import os
from django.db import models
from django.db.models.functions import Lower
from django.core.validators import FileExtensionValidator
from django.db.models import Q
from datetime import datetime as dt
from datetime import timedelta as td
import pytz

gmt=pytz.timezone('GMT')
# account model with name, username, password, email
class Account(models.Model):
    class Meta:
        db_table = "accounts"
        constraints = [
            models.UniqueConstraint(Lower('username').desc(), name='unique_username'),
            models.UniqueConstraint(Lower('email').desc(), name='unique_email')
        ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    xp = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id} : {self.username}"
    
    def get_friends(self):
        friends = Friend.objects.filter(Q(account1=self, accepted=True) | Q(account2=self, accepted=True))
        friend_list = []
        for friend in friends:
            if friend.account1.id == self.id:
                friend_list.append({"account" : friend.account2})
            else:
                friend_list.append({"account" :friend.account1})
        return friend_list

    def get_pending_requests(self):
        pending_friends = Friend.objects.filter(account2=self, accepted=False)
        friend_list = []
        for friend in pending_friends:
            if friend.account1.id == self.id:
                friend_list.append({"account" : friend.account2})
                
            else:
                friend_list.append({"account" : friend.account1})
                
        return friend_list
    
    def get_streak(self):
        date = dt.now().date()
        print(date)
        
        streak = 0
        workouts = Workout.objects.filter(Q(account=self.id))     
        while True:
            hit = False
            for w in workouts:
                test = w.endTime.replace(tzinfo=gmt)
                print(test)
                if test <= gmt.localize(dt(date.year, date.month, date.day, 23,59,59)) and \
                    test >= gmt.localize(dt(date.year, date.month, date.day, 00,00,00)):
                    hit = True
            if hit == True:
                streak += 1
                date = date - td(days=1)
            else:
                return {"streak" : streak}
        
        

# Exercises with type, datetime, accountID, video_filepath, csv_filepath

def get_video_file_path(instance, filename):
    account_id = instance.account.id
    timestamp = instance.datetime.strftime('%Y-%m-%d_%H-%M-%S')
    exercise_type = instance.exercise_type
    file_extension = os.path.splitext(filename)[1]
    return f"exercises/{account_id}/{exercise_type}/{timestamp}/video{file_extension}"

def get_csv_file_path(instance, filename):
    account_id = instance.account.id
    timestamp = instance.datetime.strftime('%Y-%m-%d_%H-%M-%S')
    exercise_type = instance.exercise_type
    file_extension = os.path.splitext(filename)[1]
    return f"exercises/{account_id}/{exercise_type}/{timestamp}/data{file_extension}"

# Exercises with id, type, datetime, account, video_file, csv_file
class Exercise(models.Model):
    class Meta:
        db_table = "exercises"
    
    id = models.AutoField(primary_key=True)
    TYPE_CHOICES = [
        ('squat', 'Squat'),
        ('bicep_curl', 'Bicep Curl'),
        ('shoulder_press', 'Shoulder Press'),
    ]
    exercise_type  = models.CharField(max_length=30, choices=TYPE_CHOICES)
    datetime = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to=get_video_file_path, 
                            null=True, 
                            name="video_file", 
                            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    csv_file = models.FileField(upload_to=get_csv_file_path, 
                                null=True, 
                                name="csv_file", 
                                validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    QUALITY_CHOICES = [
        ('unchecked', 'Unchecked'),
        ('good', 'Good'),
        ('bad', 'Bad'),
    ]
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES, default='unchecked')

    def __str__(self):
        return f'{id} : {self.account.id}/{self.exercise_type}/{self.datetime}'


# Workouts with ID, accountID, startTime, endTime
class Workout(models.Model):
    class Meta:
        db_table = "workouts"
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    xp = models.IntegerField(default=0)
    def __str__(self):
        return f"User {self.account}'s workout started at {self.startTime}, and ended at {self.endTime}."

# Friends with accountID1, accountID2, accepted
class Friend(models.Model):
    class Meta:
        db_table = "friends"
        constraints = [
            models.UniqueConstraint(fields=['account1', 'account2'], name='unique_friend'),
        ]
    account1 = models.ForeignKey(Account, related_name='friend_requests_sent', on_delete=models.CASCADE)
    account2 = models.ForeignKey(Account, related_name='friend_requests_received', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"User: {self.account1.username}. Request: {self.account2.username}. Status: {self.accepted}"

# Posts with ID, accountID, workoutID, post_datetime, title, description
class Post(models.Model):
    class Meta:
        db_table = "posts"
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    post_datetime = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"User: {self.account}, Title: {self.title}"

# Likes with accountID, postID
class Like(models.Model):
    class Meta:
        db_table = 'likes'
        constraints = [
            models.UniqueConstraint(fields=['account', 'post'], name='unique_like'),
        ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.account} likes post {self.post}."

