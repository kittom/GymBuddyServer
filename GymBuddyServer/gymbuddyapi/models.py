import os
from django.db import models
from django.db.models.functions import Lower
from django.core.validators import FileExtensionValidator

# account model with name, username, password, email
class Account(models.Model):
    class Meta:
        db_table = "accounts"
        constraints = [
        models.UniqueConstraint(Lower('username').desc(), name='unique_username'),
        models.UniqueConstraint(Lower('email').desc(), name='unique_email')
        ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.username

# Exercises with type, datetime, accountID, filepath

def get_file_path(instance, filename):
    account_id = instance.account.id
    file_extension = os.path.splitext(filename)[1]
    timestamp = instance.datetime
    return f"videos/{account_id}/{instance.type}_{timestamp}{file_extension}"

class Exercise(models.Model):
    class Meta:
        db_table = "exercises"
    type = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_file_path, 
                            null=True, 
                            name="file", 
                            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return self.file.path


# Workouts with ID, accountID, startTime, endTime
class Workout(models.Model):
    class Meta:
        db_table = "workouts"
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
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
    accepted = models.BooleanField()
    def __str__(self):
        return f"User: {self.account1}. Request: {self.account2}. Status: {self.accepted}"

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

