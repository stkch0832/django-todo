from secrets import choice
from django.db import models
from django.conf import settings
from django.utils import timezone

class Ticket(models.Model):
    TASK_STATUS = (
            ('', 'Select'),
            ('Not implemented', 'Not implemented'),
            ('In progress', 'In progress'),
            ('Pending', 'Pending'),
            ('Closed', 'Closed'),
        )
    title = models.CharField(max_length=100, help_text = 'タスク名')
    description = models.TextField(help_text='備考欄')
    task_status = models.CharField(max_length=20, choices=TASK_STATUS, help_text='ステータス')
    limit_time = models.DateTimeField(help_text='期限')
    created_at = models.DateTimeField(help_text='作成日時')
    update_at = models.DateTimeField(help_text='更新日時')

    def __str__(self):
            return self.title
