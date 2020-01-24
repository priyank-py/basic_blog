from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleReview
from .forms import ArticleForm, ArticleReviewForm

def home(request):
    articles = Article.objects.all().order_by('-published_on')
    
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
    if request.method == 'POST':

        form = ArticleReviewForm(request.POST)
        if(form.is_valid):
            data = form.save(commit=False)
            data.article = article
            data.user = request.user
            data.save()
            return redirect('each_blog', pk)
    else:
        form = ArticleReviewForm()


    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'main/each_blog.html', context)

def reviews(request):
    reviews = ArticleReview.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'main/reviews.html', context)

def create_blog(request):
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()

    return render(request, 'main/create_blog.html', {'form':form})