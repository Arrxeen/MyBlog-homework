from django.db import models
from datetime import timedelta
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date_time = models.DateTimeField(auto_now_add=True)
    id_author = models.ForeignKey( Author , on_delete=models.DO_NOTHING, related_name='posts')

    def __str__(self):
        return self.title

    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date_time


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    creat_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post_id}, {self.author_name}"