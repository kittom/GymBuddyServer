from django.contrib import admin

# Register your models here.
from .models import Account, Post, Exercise, Friend, Like, Workout

admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Exercise)
admin.site.register(Friend)
admin.site.register(Workout)
admin.site.register(Like)