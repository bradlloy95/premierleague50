from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
import requests                                      #add to requirements
import json
from .models import User

# Create your views here.
def index(request):
    
    return render(request, "fixtures/index.html", {'data':apiCall()})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "fixtures/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "fixtures/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "fixtures/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "fixtures/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "fixtures/register.html")


def apiCall():
    #API key from football-data.org
    token = 'c1536bfd2888413b84d5341baa1dc770'
    #endpoint url for pl standings
    endpoint = 'https://api.football-data.org/v4/competitions/PL/standings'
    headers = {'X-Auth-Token': token}
    
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        

        json_formatted_str = json.dumps(data, indent=2)

        print(json_formatted_str)
        
        return data

    else:
        return {'error': response.status_code}
    