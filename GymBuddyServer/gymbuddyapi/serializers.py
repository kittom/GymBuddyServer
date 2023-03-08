from rest_framework import serializers
from .models import Account, Exercise, Workout


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

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'type', 'datetime', 'account', 'file']
    
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField()
    datetime = serializers.DateTimeField()
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    file = serializers.FileField()

# class WorkoutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workout
#         fields = ['id', 'account', 'startTime', 'endTime']

#     id = serializers.IntegerField(read_only=True)
#     account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
#     startTime = serializers.DateTimeField()
#     endTime = serializers.DateTimeField()
