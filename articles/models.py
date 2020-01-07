from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):

    GENRES = (
        ('adventure', 'Adventure'),
        ('wildlife', 'Wildlife'),
        ('lifestyle', 'Lifestyle'),
        ('technology', 'Technology'),
        ('music', 'Music')
    )

    title  = models.CharField(max_length=120)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateField(default=timezone.now, blank=True, null=True)
    modified_on = models.DateField(default=timezone.now, blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRES, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title  