from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CreateUserForm, UserUpdateForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={'users': users})


class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User successfully created')


class UpdateUser(SuccessMessageMixin, UserPassesTestMixin, View):
    template_name = 'users/update.html'
    success_message = _('User successfully updated')

    # UserPassesTestMixin
    def test_func(self):
        user_pk = self.kwargs.get('pk')
        return self.request.user.pk == user_pk

    # Если нет доступа к редактированию
    def handle_no_permission(self):
        messages.error(self.request, _("You do not have permission to change another user."))
        return redirect('users')

    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_pk)
        form = UserUpdateForm(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_pk)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            new_password = form.cleaned_data.get('new_password1')
            if new_password:
                user.set_password(new_password)
                user.save()

            messages.success(request, self.success_message)
            return redirect('users')
        return render(request, self.template_name, {'form': form})


class DeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'index.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
