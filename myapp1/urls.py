"""movie URL Configuration

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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.movieview.as_view(), name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.log_in, name='log_in'),
    path('movie_list', views.movie_list, name='movie_list'),
    path('base', views.base, name='bse'),
    path('bollywood', views.base, name='bollywood'),
    path('hollywood', views.base, name='hollywood'),
    path('movie_detail/<int:pk>', views.movie_detail_view.as_view(), name='movie_d')

    #path('logout', views.logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

