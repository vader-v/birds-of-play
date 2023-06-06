from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views import View
from .models import Bird, Photo
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'amir-bullock-birds-of-play'

class Home(LoginView):
  template_name = 'home.html'

class AboutView(TemplateView):
  template_name = "about.html"

class BirdCreate(LoginRequiredMixin, CreateView):
  model = Bird
  fields = ['name', 'origin', 'description', 'times_seen']
  success_url = '/birds/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
  model = Bird
  fields = ['name', 'origin', 'description', 'times_seen']

class BirdDelete(LoginRequiredMixin, DeleteView):
  model = Bird
  success_url = '/birds/'

@login_required
def bird_index(request):
  birds = Bird.objects.filter(user=request.user)
  return render(request, 'birds/index.html', { 'birds': birds })

@login_required
def bird_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/detail.html', {'bird': bird })

class SignupView(View):
  def get(self, request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    error_message = ''
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
      form = UserCreationForm()
      context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def add_photo(request, bird_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, bird_id=bird_id)
      bird_photo = Photo.objects.filter(bird_id=bird_id)
      if bird_photo.first():
        bird_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
    return redirect('bird-detail', bird_id=bird_id)