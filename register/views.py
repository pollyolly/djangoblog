from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()

    context = {
        'registerform': form
    }
    return render(request, 'register/register.html', context)
