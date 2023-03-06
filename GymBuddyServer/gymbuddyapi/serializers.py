from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    # exercises = serializers.PrimaryKeyRelatedField(many=True, queryset=Exercise.objects.all())

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

# class ExerciseSerializer(serializers.ModelSerializer):
#     account = AccountSerializer()

#     class Meta:
#         model = Exercise
#         fields = ['type', 'datetime', 'account', 'filepath']

