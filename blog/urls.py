from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_show, name='blog_show'),
    path('<category>/', views.blog_category, name='blog_category'),
]