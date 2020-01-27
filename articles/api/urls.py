from django.urls import path
from . import views
urlpatterns = [
    path('blog-detail/<int:id>', views.get_article_view, name="blog_detail"),
]
