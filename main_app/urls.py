from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('birds/', views.bird_index, name='bird-index'),
  path('birds/create/', views.BirdCreate.as_view(), name='bird-create'),
  path('birds/<int:bird_id>/', views.bird_detail, name='bird-detail'),
  path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird-update'),
  path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird-delete'),
]