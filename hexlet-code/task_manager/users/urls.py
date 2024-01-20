from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users'),
    path('create/', views.CreateUser.as_view(), name='create'),
    path('users/<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
    path('users/<int:pk>/delete/', views.DeleteUser.as_view(), name='delete'),
]