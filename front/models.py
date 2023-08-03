from django.db import models

class TodoList(models.Model):
    status = models.BooleanField(default=False)
    todo = models.TextField()
    pubDate = models.DateTimeField('date published')

