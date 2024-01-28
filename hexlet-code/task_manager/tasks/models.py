from django.contrib.auth.models import User
from django.db import models
from task_manager.labels.models import Label
from task_manager.statuses.models import TaskStatus


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # связь один ко многим со статусами, у задачи может быть только один статус
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, null=True)
    # постановщик задачи
    creator_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_tasks')
    # исполнитель, связь один ко многим, у одной задачи может быть только один исполнитель
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='executed_tasks')
    # метки, связь многие ко многим
    labels = models.ManyToManyField(Label, through='TaskLabel')


# промежуточная модель в, m2m, чтобы запретить удаление метки, если назначана на задачу
class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('task', 'label')
