from pathlib import Path

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .users import forms
from django.utils.translation import gettext_lazy as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = forms.LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main')
    success_message = _('You are logged in')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if 'next' in request.GET:
            messages.error(request, _('You are not authorized! Please log in.'))
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('login'))
