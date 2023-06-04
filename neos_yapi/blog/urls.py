from django.urls import path
from .import views



urlpatterns=[
    path('blogs/', views.blog, name="blog"),
    path('post_detail/<int:pk>/', views.post_detail, name="blog-post-detail"),
    path('post_edit/<int:pk>/', views.post_edit, name="blog-post-edit"),
    path('post_delete/<int:pk>/', views.post_delete, name="blog-post-delete"),
    path('comment_delete/<int:pk>/', views.comment_delete, name="blog-comment-delete"),
    path('comment_edit/<str:pk>/', views.comment_edit, name="blog-comment-edit"),
    path('search_bar/', views.search_bar, name="blog-search"),
]