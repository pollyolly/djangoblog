"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import debug_toolbar
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('_debug_/', include(debug_toolbar.urls)),
    path('tinymce/', include('tinymce.urls')),
    path('', include('base.urls')),
    path('', include('blogpost.urls')),
    path('', include('setting.urls')),
    path('', include('chat.urls')),
    path('', include('register.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'djangoblog.views.handler404'
handler400 = 'djangoblog.views.handler404'
handler403 = 'djangoblog.views.handler404'

