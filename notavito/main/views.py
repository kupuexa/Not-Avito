from django.shortcuts import render, redirect
from .forms import PostForm, UserRegistrationForm, User
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


def test(request):
    return render(request, template_name="main/footer.html")


def home(request):
    return render(request, 'main/home.html', context={
        'url1':pposts[0].photo,
        'url2':pposts[1].photo,
        'url3':pposts[2].photo,
        'url4':pposts[3].photo,
        'url5':pposts[4].photo,
        'url6':pposts[5].photo,
        'url7':pposts[6].photo,
        'url8':pposts[7].photo
        })