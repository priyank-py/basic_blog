from django.urls import path
from . import views
urlpatterns = [
    path('blog-detail/<int:id>', views.get_article_view, name="blog_detail"),
    path('add-blog', views.add_article_view, name="add_blog"),
    path('update/<int:id>', views.update_article_view, name="update_article")
]
