from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles.models import Article
from articles.api.serializer import ArticleSerializer

@api_view(['GET',])
def get_article_view(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
