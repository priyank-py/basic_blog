from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('contact-us', views.contact_us, name="contact"),
    path('blog/<int:pk>', views.each_blog, name="each_blog"),
    path('reviews', views.reviews, name="all_reviews"),
]
