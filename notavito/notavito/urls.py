"""notavito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main.views import create_post, search, edit_post, registration, delete_post, profile,registration,post, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('search', search, name='search'),
    path('post/', post),
    # path('post/<int: post_id>/edit', ...),
    # path('login', ...),
    path('registration', registration),
    path('post_create', create_post),
    path('post/<int:post_id>/delete', delete_post, name='delete_post'),
    path('post/<int:post_id>/edit', edit_post),
    path('profile/', profile)
]
