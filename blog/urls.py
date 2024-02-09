from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.index, name="posts"),
    path('post/<int:pk>/', views.post_details, name="post_details"),
    path('category/<category>/', views.category_post, name="category_posts")
]
