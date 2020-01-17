from django import forms
from .models import ArticleReview


class ArticleReviewForm(forms.ModelForm):
    class Meta:
        model = ArticleReview
        fields = ('stars', 'feedback')