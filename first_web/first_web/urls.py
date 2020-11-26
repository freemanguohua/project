"""first_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from myapp import views as app_views

urlpatterns = [
    path('myapp/', app_views.register,name = 'myapp'),
    path('example/', app_views.example,name='example'),
    path('pos_download/', app_views.pos_download, name='pos_download'),
    path('neg_download/', app_views.neg_download, name='neg_download'),
    path('^admin/', admin.site.urls),
    #url(r'^app/$', app_views.register),
    #url(r'^admin/', admin.site.urls),
]
