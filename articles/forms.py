from django import forms
from .models import Article, ArticleReview


class ArticleValidationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
    def clean_title(self, *args, **kwargs):
        data = self.cleaned_data
        title = data.get('title')
        if len(title) > 50:
            raise forms.ValidationError('Article Title cannot be more than 50 characters')

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        title_image = data.get('title_image')
        body = data.get('body')
        if body == '':
            body = None
        if title_image is None and body is None:
            raise forms.ValidationError('There must be blog image or text content in the body!')


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