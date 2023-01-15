from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# temtplates/base/
def handler404(request, exception=None, template_name='base/404.html'):
    return render(request, template_name, {'status':'404'})
