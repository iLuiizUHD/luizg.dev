from django.urls import path

from . import views

urlpatterns = [
    path('', views.Blog.as_view(), name="blog"),
    path('posts/post/<slug:slug>', views.BlogPost.as_view(), name="blog_post"),
    path('posts/new', views.NewBlogPost.as_view(), name="new_blog_post"),
]
