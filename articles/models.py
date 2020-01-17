from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def upload_to(instance, filename):
    return f'{instance.writer.username}/{filename}'


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
    title_image = models.ImageField(upload_to=upload_to,  blank=True, null=True)
    published_on = models.DateField(default=timezone.now, blank=True, null=True)
    modified_on = models.DateField(default=timezone.now, blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRES, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class ArticleReview(models.Model):

    STARS = (
        ('one', '1 Star'),
        ('two', '2 Star'),
        ('three', '3 Star'),
        ('four', '4 Star'),
        ('five', '5 Star'),
    )

    article = models.ForeignKey(Article, verbose_name="article", related_name="reviews", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, related_name="user_reviews", verbose_name="Reviewer", on_delete=models.DO_NOTHING)
    stars = models.CharField(_("Stars"), max_length=50, choices=STARS, blank=True, null=True)
    feedback = models.TextField(_("Feedback"), blank=True, null=True)