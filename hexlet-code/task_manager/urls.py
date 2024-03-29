from django.contrib import admin
from django.urls import path, include
from . import views
from .views import test_rollbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='main'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('test-rollbar/', test_rollbar, name='test_rollbar'),
]
