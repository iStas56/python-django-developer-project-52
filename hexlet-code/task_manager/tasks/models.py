from django.contrib.auth.models import User
from task_manager.statuses.models import TaskStatus
from django.db import models


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

