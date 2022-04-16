from django.shortcuts import render
from blogpost.models import Post
from setting.models import Setting

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
            }
    return render(request, 'base/home.html', context)

def editpost(request, pk):
    pass 
