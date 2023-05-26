from django.shortcuts import render, redirect
from .forms import PostForm, UserRegistrationForm, User
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


def test(request):
    return render(request, template_name="main/footer.html")

def profile(request):
    id = request.GET.get("id", 0)
    user = User.objects.all()
    user = user.filter(
        id=id
    )
    if (user.exists()):
        for profile in user:
            print(f"{profile.id} {profile.username} {profile.first_name} {profile.last_name} {profile.last_login}")
    else:
        id = 0
    if id == 0:
        return render(request, 'main/profile.html', context={
            'id': 'None',
            'username': 'None',
            'first_name': 'None',
            'last_name': 'None',
            'email': 'None',
            'last_login': 'None'
        })
    else:
        return render(request, 'main/profile.html', context={
            'id': profile.id,
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'email': profile.email,
            'last_login': profile.last_login})

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