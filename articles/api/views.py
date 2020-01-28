from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles.models import Article
from articles.api.serializer import ArticleSerializer

#RETRIVE
@api_view(['GET',])
def get_article_view(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

# ADD
@api_view(['POST',])
def add_article_view(request):
    article = Article()
    
    if request.method == "POST":
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            # data["success"] = 'Article Added'
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# UPDATE
@api_view(["PUT",])
def update_article_view(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Article Updated!"
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
