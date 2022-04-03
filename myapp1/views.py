from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import User,movie,m_rating
# Create your views here.

from django.http import HttpResponse

class movieview(View):
    def get(self, request):
        Bol = movie.objects.filter(movie_ge='B')
        Hol = movie.objects.filter(movie_ge='H')
        return render(request, 'myapp1/index.html', {'Bol': Bol, 'Hol': Hol}) #white match to bol variable



#def home(request):
    #return render(request, 'myapp1/index.html')

#def movie_detail(request):
    #return render(request, 'myapp1/movie_detail.html')

class movie_detail_view(View):
    def get(self, request, pk):
        mo = movie.objects.get(pk=pk)
        return render(request, 'myapp1/movie_detail.html', {'mo':mo})

def signup(request):
    if request.method == "POST":
        username = request.POST['userid']
        email = request.POST['email']
        password = request.POST['psw']
        password1 = request.POST['psw-repeat']
        uname = request.POST['name']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = uname
        myuser.save()
        messages.success(request, 'successfully register')
        return redirect('/login')

    return render(request, 'myapp1/signup.html')

def movie_list(request):
    return render(request, 'myapp1/movie_list.html')

def base(request):
    return render(request, 'myapp1/base.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            uname = user.first_name
            return render(request, 'myapp1/index.html', {'uname': uname})
        else:
            messages.error(request, 'invalid login')
            return redirect('home')
    return render(request, 'myapp1/login.html')
