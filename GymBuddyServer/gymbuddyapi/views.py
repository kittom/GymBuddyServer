from .models import Account, Exercise, Workout
from .serializers import AccountSerializer, ExerciseSerializer, WorkoutSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import ExerciseSerializer
import asyncio

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ExerciseView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            video_file = serializer.validated_data['video_file']
            csv_file= serializer.validated_data['csv_file']
            serializer.save(video_file=video_file, csv_file=csv_file)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExerciseList(generics.ListAPIView):
    
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        account_id = self.kwargs['account']
        print(account_id)
        return Exercise.objects.filter(account__id=account_id)

# class WorkoutList(generics.ListAPIView):
#     serializer_class 


class WorkoutCreate(generics.CreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
class WorkoutList(generics.ListAPIView):
    
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        account_id = self.kwargs['account']
        return Workout.objects.filter(account=account_id)

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
class ExerciseByWorkoutView(generics.ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        workout_id = self.kwargs['workout_id']
        workout = Workout.objects.get(id=workout_id)
        return Exercise.objects.filter(account=workout.account, datetime__range=(workout.startTime, workout.endTime))