from django.conf import settings
from django.db import models

POST_STATUS_CHOICES = (
            (1, '未着手'),
            (2, '進行中'),
            (3, '保留'),
            (4, '完了'),
            (5, '中止'),
        )

POST_PRIORITY_CHOICES = (
            (1, '緊急・重要'),
            (2, '緊急'),
            (3, '重要'),
            (4, '期限内'),
            (5, '期限なし'),
        )

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タスク名", max_length=20)
    status = models.IntegerField("ステータス", choices=POST_STATUS_CHOICES)
    priority = models.IntegerField("優先度", choices=POST_PRIORITY_CHOICES)
    limit_datetime = models.DateTimeField("期限")
    description = models.TextField("詳細")

    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.title
