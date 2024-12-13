from django.db import models


class Career(models.Model):
    username = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    content = models.TextField()