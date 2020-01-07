from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
