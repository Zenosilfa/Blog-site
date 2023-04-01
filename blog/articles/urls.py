from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "articles"

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.Addarticle,name="addarticle"),
    path('article/<int:id>', views.detail,name="detail"),
    path('update/<int:id>', views.updateArticle,name="updateArticle"),
    path('delete/<int:id>', views.deleteArticle,name="delete"),
    path('', views.viewarticles,name="viewarticles"),
    path('comment/<int:id>', views.addComment,name="comment"),
    
]

