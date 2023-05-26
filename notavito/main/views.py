from django.shortcuts import render, redirect
from .forms import PostForm, UserRegistrationForm, User
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


def test(request):
    return render(request, template_name="main/footer.html")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return HttpResponse("Успешно")
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})


def search(request):
    search_word = request.GET.get('search')
    try:
        if len(founded_posts := Post.objects.filter(title__icontains=search_word)) != 0:
            return render(request, 'main/search_page.html', context={'posts': founded_posts})
        else:
            return render(request, 'main/not_founded.html')
    except:
        return render(request, 'main/not_founded.html')


def delete_post(request, post_id):
    post_object = get_object_or_404(Post, id=post_id)  # если не нашел отправить 404
    if request.method == "POST":
        post_object.delete()
        return render(request, template_name='main/success_deleted.html')


def edit_post(request, post_id):
    record = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=record)
    return render(request, 'edit_record.html', {'form': form, 'record': record})
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