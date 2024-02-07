from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.index, name="posts")
]
