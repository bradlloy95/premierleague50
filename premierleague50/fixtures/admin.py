from django.contrib import admin
from .models import User, Team,Fixture
# Register your models here.

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Fixture)