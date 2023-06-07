from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.AboutView.as_view(), name='about'),
  path('accounts/signup/', views.SignupView.as_view(), name='signup'),
  path('birds/', views.BirdIndex.as_view(), name='bird-index'),
  path('birds/create/', views.BirdCreate.as_view(), name='bird-create'),
  path('birds/<int:bird_id>/', views.BirdDetail.as_view(), name='bird-detail'),
  path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),
  path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),
  path('add-photo/<int:bird_id>/', views.AddPhotoView.as_view(), name='add-photo'),
]