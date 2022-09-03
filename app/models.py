from django.conf import settings
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タスク名", max_length=20)
    status = models.IntegerField("ステータス")
    priority = models.IntegerField("優先度")
    limit_datetime = models.DateTimeField("期限")
    description = models.TextField("詳細")

    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.title
