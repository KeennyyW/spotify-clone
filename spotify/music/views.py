from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout, authenticate, login

#from django.http import HttpResponse  
# Create your views here.

@login_required(login_url="login")
def index(request):
    return render(request, "music/index.html")


def login(request):
    if request.method == "POST":
        
        # gets username and password via POST data

        username = request.POST.get("username") 
        password = request.POST.get("password")

        # checks if user is already registered 

        user = authenticate(request, username=username, password=password)

        # if the user exists they will be logged in and redirected

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "User not found")
            return redirect("login")
        
    else:
        return render(request, "music/login.html")

def signup(request):
    if request.method == "POST":

        #defining userdata

        username = request.POST.get("username") 
        email = request.POST.get("email") 
        password = request.POST.get("password") 
        password2 = request.POST.get("password2") 

        # check if password is the same

        if password2 == password:

            # check if the email or the username is already in the database

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("signup")
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("signup")
            
            # creates new user 

            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect("/")
        else: 
            messages.info(request, "Password Not Matching")
            return redirect("signup")

    else:
        return render(request, "music/signup.html")


@login_required(login_url="login")
def logout_func(request):
    auth.logout(request)
    return redirect("signup")



def logout():
    pass