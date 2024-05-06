from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Team(models.Model):
    name = models.CharField(max_length=50)
    crest = models.URLField()
    stadium = models.CharField(max_length=100)
    colors = models.CharField(max_length=50)
    mananger = models.CharField(max_length=100)
    ranking = models.IntegerField(null=True)
    played = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    lastUpdate = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Team: {self.name}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'stadium': self.stadium,
            'colors': self.colors,
            'manager': self.mananger,
            'ranking': self.ranking,
            'played': self.played,
            'points': self.points,
            'lastUpdate': self.lastUpdate
        }

class Fixture(models.Model):
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="homeTeam")
    homeTeamScore = models.CharField(max_length=10, null=True)
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="awayTeam")
    awayTeamScore = models.CharField(max_length=10, null=True)
    
    fulltime = models.BooleanField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.homeTeam} vs {self.awayTeam} on {self.date}"
    
    def serialize(self):
        return {'id':self.id,
                'hometeam': self.homeTeam.name,
                'awayteam': self.awayTeam.name,
                'homeScore': self.homeTeamScore,
                'awayScore': self.awayTeamScore,
                'fulltime': self.fulltime,
                'date': self.date.strftime('%y-%m-%d')}
        
        
# class Player(models.Model):
#     name = models.CharField(max_length=100)
    