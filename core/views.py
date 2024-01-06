from django.shortcuts import render
from django.contrib.auth.models import User, auth
import json
from django.contrib import messages
from django.http import HttpResponse

# render() function, which is used to send back an HttpResponse object with the
# content of the template rendered with the given context.
# from django.http import HttpResponse 
# HttpResponse object, which is used to send back an HTTP response to the client.
# The HttpResponse object is instantiated with the content that will be sent back
# to the client, which in this case is a simple string that contains the text
# "Welcome to social book".

# Create your views here.

def index(request):
    return render(request, 'index.html')
# this function
# takes an HttpRequest object as its first parameter, which is typically named request.
# This object contains information about the current Web request that has triggered 
# this view, including the requested URL, any data sent in the request, and more.
# The view function returns an HttpResponse object that contains the content that
# the user will see in their browser. In this case, the content is a simple string
# that contains the text "Welcome to social book". The HttpResponse object is then
# sent back to the client, which will display the content in the user's browser.


def signup(request):
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email already exist")
                return render(request, 'signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return render(request, 'signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, "User Created")
        
        else:
            messages.info(request, "Password not Matched")
            return render(request, 'signup')
        
        
    else:
        return render(request, 'signup.html')
    



