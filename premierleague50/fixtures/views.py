from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
import requests                                      #add to requirements
import json
from .models import User, Team, Fixture
from django.utils import timezone
from datetime import timedelta

# set variables for dates
current_date = timezone.localdate() 
current_date_viewed = current_date

# Create your views here.
def index(request):
    """
    loads the home page-
        
    """
    global current_date
    global current_date_viewed
    
    #update database every 24 hours
    team = Team.objects.get(name = 'Arsenal FC')
    if team.lastUpdate != current_date:
        print('update')
        RunUpdates()
        
    else:
        print('same')
    
    current_date_index = timezone.localdate() 
    current_date = current_date_index
    current_date_viewed = current_date
    
    return render(request, "fixtures/index.html", {'data':apiCallStandings(),
                                                   'date':current_date_index,
                                                   'fixtures':apiCallFixtures(current_date)})



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

def teams_view(request, team_id):
    print(team_id)
    
    return render(request, "fixtures/teams.html", {'data': apiCallTeams(team_id)})



import creds

#apis
def apiCallStandings():
    #API key from football-data.org
    #token = 'c1536bfd2888413b84d5341baa1dc770'
    #endpoint url for pl standings
    endpoint = 'https://api.football-data.org/v4/competitions/PL/standings'
    headers = {'X-Auth-Token': creds.token}
    
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
            
        return data

    else:
        
        return {'error': response.status_code}

def apiCallFixtures(date):
     #API key from football-data.org
    
    #token = 'c1536bfd2888413b84d5341baa1dc770'
    #endpoint url for pl standings
    dateFrom = '2024-01-01'
    endpoint = f'http://api.football-data.org/v2/competitions/2021/matches?dateFrom={str(date)}&dateTo={str(date)}'
    headers = {'X-Auth-Token': creds.token}
    
    response = requests.get(endpoint, headers=headers)
    #print(endpoint)
    #print(date)
    serialized_data =[]
    
    if response.status_code == 200:
        data = response.json()
        # for i in data['matches']:
        #     i['homeTeam']['crest'] = getCrest(i['homeTeam']['id'])
        #     i['awayTeam']['crest'] = getCrest(i['awayTeam']['id'])
            
            
            
        #print(data)       
      
        return data

    else:
        return {'error': response.status_code}
    
def apiCallTeams(id):
    
    #token = 'c1536bfd2888413b84d5341baa1dc770'
    #endpoint url for pl standings
    endpoint = f"https://api.football-data.org/v4/teams/{str(id)}"

    headers = {'X-Auth-Token': creds.token}
    
    
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        data = response.json()   
        team = Team.objects.get(name=data['name'])      
        print(team.lastUpdate)   
        return data
    else:
        return {'error': response.status_code}
    

        
    
def getFixtures(request):
    global current_date_viewed    
    
    #print('date', request.GET.get('dateViewed'))    
    
    if request.GET.get('day') == 'yesterday':
        
        yesterday = current_date_viewed - timedelta(days=1)
        current_date_viewed = yesterday
        DBdata = Fixture.objects.filter(date=yesterday)
        count = len(DBdata)
        print(count)
        
        serialized =[{'serialized':match.serialize()} for match in DBdata]
        
        response_Data = {'serialized': serialized,
                         'dateViewed': current_date_viewed,
                         'count':count}
        
        print(serialized)
        #data = apiCallFixtures(yesterday)
        #print(data)
        
        return JsonResponse(response_Data, safe=False)
       
        
    else:
        tommorrow = current_date_viewed + timedelta(days=1)
        current_date_viewed = tommorrow
        DBdata = Fixture.objects.filter(date=tommorrow)
        count = len(DBdata)
                
        serialized =[{'serialized':match.serialize()} for match in DBdata]
        
        response_Data = {'serialized': serialized,
                         'dateViewed': current_date_viewed,
                         'count':count}
        
        print(serialized)
        #data = apiCallFixtures(yesterday)
        #print(data)
        
        return JsonResponse(response_Data, safe=False)
    
  
    
def RunUpdates():
    token = creds.token
    #endpoint url for pl standings
    #endpoint = 'https://api.football-data.org/v4/competitions/PL/teams'

    headers = {'X-Auth-Token': token}
    
    # response = requests.get(endpoint, headers=headers)
    
    # if response.status_code == 200:
    #     data = response.json()
    #     for team in data['teams']:
            
    #         print(data)
    #         name = team['name']
    #         stadium = (team['venue'])
    #         crest = (team['crest'])
    #         manager = (team['coach']['name'])
    #         colors = (team['clubColors'])
            
    #         TEAM = Team(name=name,
    #                     stadium=stadium,
    #                     crest=crest,
    #                     mananger=manager,
    #                     colors=colors)
    #         TEAM.save()
    # else:
    #     
    
    """table data"""
    endpoint = 'https://api.football-data.org/v4/competitions/PL/standings'
    response = requests.get(endpoint, headers=headers)
    
    
    if response.status_code == 200:
        data = response.json()
        for standing in data['standings']:
            for team in standing['table']:
                TEAM = Team.objects.get(name=team['team']['name'])
                TEAM.ranking = team['position']
                TEAM.played = team['playedGames']
                TEAM.points = team['points']
                TEAM.save()
      

    else:
        pass
    
    """Fixture data"""
    endpoint = f'http://api.football-data.org/v2/competitions/2021/matches'
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        Fixture.objects.all().delete()
        
        data = response.json()
        for match in data['matches']:
            print(match)
            homeTeam = Team.objects.get(name = match['homeTeam']['name'])   

            awayTeam = Team.objects.get(name=match['awayTeam']['name'])
            status = None
            if match['status'] == 'SCHEDULED':
                status = False
            else:
                status = True
                
            homeTeamScore = (match['score']['fullTime']['homeTeam']) #home team
            awayTeamScore = (match['score']['fullTime']['awayTeam']) #away team
            date = match['utcDate'].split('T')[0]   
            FIXTURE = Fixture(homeTeam=homeTeam,
                              awayTeam=awayTeam,
                              homeTeamScore=homeTeamScore,
                              awayTeamScore=awayTeamScore,
                              fulltime=status,
                              date=date
                              )
            FIXTURE.save()
        
    else:
        pass
    
    
"""next-
create model for players
remove api calls and use database for frontend

"""  