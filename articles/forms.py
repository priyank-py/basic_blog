from django import forms
from .models import Article, ArticleReview


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog title here...'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model = Article
        fields = '__all__'

class ArticleReviewForm(forms.ModelForm):
    class Meta:
        model = ArticleReview
        fields = ('stars', 'feedback')