from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def addcomment(request,pk):
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and request.POST:
       postinstance = Post.objects.get(id=pk)
       newcomment = form.save(commit=False)
       newcomment.post = postinstance
       newcomment.name = request.POST.get('name')
       newcomment.comment = request.POST.get('comment')
       newcomment.save()
       messages.success(request, 'Comment has been added!')
    else:
       messages.warning(request, 'You have an emtpy comment.')
def post(request, pk):
    post = Post.objects.get(id=pk)
    #comment = Comment.objects.filter(post=pk).order_by('-created')[:5]

    commentall = Comment.objects.filter(post=pk).order_by('-created')
    paginator = Paginator(commentall, 3)

    page_number = request.GET.get('page')
    comment = paginator.get_page(page_number)

    commentform = CommentForm(postid=pk)
    addcomment(request,pk)
    context = {
       #'page_obj':page_obj,
       'post':post,
       'commentform': commentform,
       'comments': comment,
       'totalcomment':commentall,
       'user_auth':request.user.is_authenticated
    }
    return render(request, 'blogpost/blogpost.html', context)
def editpost(request, pk):
    pass #null
