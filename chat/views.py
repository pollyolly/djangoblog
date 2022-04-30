from django.shortcuts import render
from .forms import ChatForm
# Create your views here.

def chats(request):
    form = ChatForm
    context = {
    'chatform': form
    }
    return render(request, 'chat/chat.html', context)
