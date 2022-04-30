from django.shortcuts import render
from blogpost.models import Post, Tag
from setting.models import Setting

# Create your views here.
def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.prefetch_related('tag').all() #cache and query; note if filter added cache will not work
    #for post in posts:
    #    testing =[post.tag.all()]
    context = {
        'posts':posts,
    }
    return render(request, 'base/home.html', context)

def editpost(request, pk):
    pass 
