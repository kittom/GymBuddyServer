from rest_framework import serializers
from .models import Account, Exercise, Workout, Post, Friend, Like

class AccountSerializer(serializers.ModelSerializer):
    # exercises = serializers.PrimaryKeyRelatedField(many=True, queryset=Exercise.objects.all())

    class Meta:
        model = Account
        fields = ['id','first_name', 'last_name', 'username', 'password', 'email']
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'username']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'exercise_type', 'datetime', 'account','quality', 'video_file', 'csv_file']
    
    id = serializers.IntegerField(read_only=True)
    exercise_type = serializers.CharField()
    datetime = serializers.DateTimeField()
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    quality = serializers.CharField()
    video_file = serializers.FileField()
    csv_file = serializers.FileField()

class ExerciseQualityUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['quality']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'account', 'startTime', 'endTime', 'title', 'description']

    id = serializers.IntegerField(read_only=True)
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    title = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)

class FriendSerializer(serializers.ModelSerializer):
    account1 = AccountSerializer()
    account2 = AccountSerializer()

    class Meta:
        model = Friend
        fields = ['account1', 'account2', 'accepted']

class FriendGetSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = Friend
        fields = ['account']

class PostSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    workout = WorkoutSerializer()

    class Meta:
        model = Post
        fields = ['account', 'workout', 'post_datetime', 'title', 'description']

class LikeSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    post = PostSerializer()

    class Meta:
        model = Like
        fields = ['account', 'post']
