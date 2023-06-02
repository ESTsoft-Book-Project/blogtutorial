"""
URL configuration for blogtutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from blog.views import Index, DetailArticleView, LikeArticle, DeleteArticle, Featured

urlpatterns = [
    # root path => blog/templates/blog/index.html
    # {% url 'index' %} will lead user index.html
    path("", Index.as_view(), name="index"),
    path("featured/", Featured.as_view(), name="featured"),
    path("tinymce/", include("tinymce.urls")),
    path("<int:pk>/", DetailArticleView.as_view(), name="detail_article"),
    path("<int:pk>/like", LikeArticle.as_view(), name="like_article"),
    path("<int:pk>/delete", DeleteArticle.as_view(), name="delete_article"),
]
