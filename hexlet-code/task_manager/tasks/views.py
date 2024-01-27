from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.translation import gettext_lazy as _
from .forms import CreateTaskForm
from .models import Task


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', context={'tasks': tasks})


class CreateTask(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Task created success')
    template_name = 'tasks/create.html'

    def get(self, request, *args, **kwargs):
        form = CreateTaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator_by = request.user
            task.save()
            messages.success(request, self.success_message)
            return redirect('tasks')
        return render(request, self.template_name, {'form': form})


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Task updated success')
    template_name = 'tasks/update.html'

    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = CreateTaskForm(instance=task)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect('tasks')
        return render(request, self.template_name, {'form': form})


class DeleteTask(LoginRequiredMixin, View):
    success_message = _('Task deleted successfully')
    template_name = 'tasks/delete.html'

    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, self.template_name, {'task': task})

    def post(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        messages.success(request, self.success_message)
        return redirect('tasks')


class DetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        return render(request, 'tasks/detail.html', {'task': task})