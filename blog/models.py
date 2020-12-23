from django.db import models
#this imports a custom user model
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'post: {self.title}, by {self.author}'
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    