from django.shortcuts import render
from .forms import ChatForm
# Create your views here.

def chats(request, room_name):
    form = ChatForm
    context = {
    'chatform': form,
    'room_name':room_name
    }
    return render(request, 'chat/chat.html', context)
