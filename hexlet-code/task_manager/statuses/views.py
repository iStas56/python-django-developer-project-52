from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TaskStatus
from .forms import CreateStatusForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        statuses = TaskStatus.objects.all()
        return render(request, 'statuses/index.html', context={'statuses': statuses})


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Status created success')
    template_name = 'statuses/create.html'

    def get(self, request, *args, **kwargs):
        form = CreateStatusForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateStatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect('statuses')
        return render(request, self.template_name, {'form': form})


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Status updated success')
    template_name = 'statuses/update.html'

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(TaskStatus, pk=status_pk)
        form = CreateStatusForm(instance=status)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(TaskStatus, pk=status_pk)
        form = CreateStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect('statuses')
        return render(request, self.template_name, {'form': form})


class DeleteStatus(LoginRequiredMixin, View):
    success_message = _('Status deleted successfully')
    template_name = 'statuses/delete.html'

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(TaskStatus, pk=status_pk)
        return render(request, self.template_name, {'status': status})

    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(TaskStatus, pk=status_pk)

        try:
            status.delete()
        except ProtectedError:
            messages.error(request, _("Cannot delete status it's in use"))
            return redirect('tasks')

        messages.success(request, self.success_message)
        return redirect('statuses')


