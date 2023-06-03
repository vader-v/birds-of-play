from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('birds/', views.bird_index, name='bird-index'),
  path('birds/create/', views.BirdCreate.as_view(), name='bird-create'),
]