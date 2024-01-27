from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='tasks'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete_task'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_task'),
]