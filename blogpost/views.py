from django.shortcuts import render
from blogpost.models import Post
# Create your views here.
def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
       'post':post,
       'user_auth':request.user.is_authenticated
    }
    return render(request, 'blogpost/blogpost.html', context)
def editpost(request, pk):
    pass #null
