from django.shortcuts import render
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
