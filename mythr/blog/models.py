from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140, null=False)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})

    def __str__(self):
        return f"<Post('{self.title}, {self.author}')>"


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment('{self.content}', '{self.post}', '{self.author}')"

