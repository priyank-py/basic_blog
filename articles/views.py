from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')

def each_blog(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {
        'article': article
    }
    return render(request, 'main/each_blog.html', context)
