from .models import Account, Exercise
from .serializers import AccountSerializer
from rest_framework import generics


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# class ExercisetList(generics.ListCreateAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer


# class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer

