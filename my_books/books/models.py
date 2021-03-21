from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
