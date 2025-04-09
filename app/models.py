from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.id)


