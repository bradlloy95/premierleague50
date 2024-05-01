from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:team_id>", views.teams_view, name="teams_view"),
    
    
    
    path("getFixtures", views.getFixtures, name="getFixtures"),
]