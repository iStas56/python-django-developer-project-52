from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Label
from .forms import CreateLabelForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/index.html', {'labels': labels})


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Label created success')
    template_name = 'labels/create.html'

    def get(self, request, *args, **kwargs):
        form = CreateLabelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateLabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect('labels')
        return render(request, self.template_name, {'form': form})


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, View):
    success_message = _('Label updated success')
    template_name = 'labels/update.html'

    def get(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_pk)
        form = CreateLabelForm(instance=label)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_pk)
        form = CreateLabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(request, self.success_message)
            return redirect('labels')
        return render(request, self.template_name, {'form': form})


class DeleteLabel(LoginRequiredMixin, View):
    success_message = _('Label deleted successfully')
    template_name = 'labels/delete.html'

    def get(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_pk)
        print(label)
        return render(request, self.template_name, {'label': label})

    def post(self, request, *args, **kwargs):
        label_pk = kwargs.get('pk')
        label = get_object_or_404(Label, pk=label_pk)

        try:
            label.delete()
        except ProtectedError:
            messages.error(request, _("Cannot delete label it's in use"))
            return redirect('tasks')

        messages.success(request, self.success_message)
        return redirect('labels')
