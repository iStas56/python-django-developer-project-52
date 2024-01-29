import django_filters
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from .models import Task, TaskStatus
from task_manager.statuses.models import TaskStatus
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=TaskStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label=_('Status')
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label=_('Executor')
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label=_('Labels')
    )
    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        widget=forms.CheckboxInput,
        label=_('Only your tasks')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_tasks']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(executor=self.request.user)
        return queryset
