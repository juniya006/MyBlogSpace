from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Blog
from django.contrib.auth import logout
# Create your views here.


def default(request):
    return render(request,'base.html')
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        newRow_objects = User.objects.create_user(username=username,email=email,password=password)
    return render(request,'register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html ')

def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']

        newRow_objects = Blog.objects.create(
            author=request.user,
            title=title,
            content=content,
            image=image
        )

    return render(request, 'add_blog.html')

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    return render(request, 'blog_detail.html', {
        'blog': blog
    })

def logout_user(request):
    logout(request)
    return redirect('home')