"""OnlineIde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.views import static 
from django.conf import settings 
from django.conf.urls import url 


from . import views

urlpatterns = [
    path('', views.Index),
    path('runcode', views.RunCode),
    path('getans', views.GetAns),
    path('connect', views.Connect),
    path('ping', views.Ping),
    path('runner', views.RunnerInfo),
    #path('wrk', views.Wrk),
    url(r'^static/(?P<path>.*)$', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]


handler404 = views.NotFound
handler500 = views.NotFound
handler403 = views.NotFound
handler400 = views.NotFound