from .models import Account, Exercise, Workout, Friend, Post, Like
from .serializers import (AccountSerializer, ExerciseSerializer, ExerciseQualityUpdateSerializer, WorkoutSerializer, 
                          FriendSerializer, PostSerializer, LikeSerializer, FriendGetSerializer, StreakGetSerializer, AccountXpUpdateSerializer)
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExerciseSerializer
from ml_analysis.knn import KNNClassifier
from ml_analysis.training_data import training_data
from ml_analysis.Exercise import ML_Exercise
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Account
from django.shortcuts import get_object_or_404


squat_classifier = KNNClassifier(training_data)
squat_classifier.train()
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = serializer.data
        response_data['friends'] = FriendGetSerializer(instance.get_friends(), many=True).data
        response_data['pending_requests'] = FriendGetSerializer(instance.get_pending_requests(), many=True).data
        response_data['streak'] = StreakGetSerializer(instance.get_streak()).data['streak']
        return JsonResponse(response_data)

@csrf_exempt
def search_accounts(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        if query:
            results = Account.objects.filter(Q(username__icontains=query)).values()
            return JsonResponse(list(results), safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


class ExerciseView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            video_file = serializer.validated_data['video_file']
            csv_file = serializer.validated_data['csv_file']
            # exercise_type = serializer.validated_data['exercise_type']
            # datetime = serializer.validated_data['datetime']
            # account = serializer.validated_data['account']

            serializer.save(video_file=video_file, csv_file=csv_file)

            instance = serializer.instance
            ex = ML_Exercise([instance.id, instance.exercise_type, instance.datetime,
                           instance.account.id, instance.video_file, instance.csv_file, instance.quality], "apple")
            prediction = squat_classifier.predict([ex])
            # Update the quality field based on the prediction
            if prediction[0] == 1:
                prediction = "good"
            else:
                prediction = "bad"
            updated_data = {
                'quality': prediction  # prediction is 'unchecked', 'good', or 'bad'
            }

            # Create a new serializer instance with the fetched object and the updated data
            update_serializer = ExerciseQualityUpdateSerializer(instance, data=updated_data, partial=True)

            if update_serializer.is_valid():
                updated_instance = update_serializer.save()

                # Serialize the updated instance using the original ExerciseSerializer
                final_serializer = ExerciseSerializer(updated_instance)

                return Response(final_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ExerciseList(generics.ListAPIView):
    
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        account_id = self.kwargs['account']
        print(account_id)
        return Exercise.objects.filter(account__id=account_id)

class WorkoutCreate(APIView):
    queryset = Workout.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            instance = serializer.instance
            account_update = AccountXpUpdateSerializer(instance.account, data={"xp": instance.account.xp + instance.xp}, partial=True)
            if account_update.is_valid():
                account_update.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(account_update.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    
class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class FriendRequest(APIView):
    def post(self, request):
        account1_id = request.query_params.get('account1', None)
        account2_id = request.query_params.get('account2', None)

        if not account1_id or not account2_id:
            return JsonResponse({'error': 'Both account1 and account2 must be provided'}, status=400)

        account1 = get_object_or_404(Account, id=account1_id)
        account2 = get_object_or_404(Account, id=account2_id)

        if account1 == account2:
            return JsonResponse({'error': 'Cannot send friend request to oneself'}, status=400)

        friend_request, created = Friend.objects.get_or_create(account1=account1, account2=account2)
        if created:
            friend_request.save()
            return JsonResponse({'message': 'Friend request sent'})

        if friend_request.accepted:
            return JsonResponse({'message': 'Already friends'})

        friend_request.accepted = True
        friend_request.save()
        return JsonResponse({'message': 'Friend request accepted'})

    def delete(self, request):
        account1_id = request.query_params.get('account1', None)
        account2_id = request.query_params.get('account2', None)

        if not account1_id or not account2_id:
            return JsonResponse({'error': 'Both account1 and account2 must be provided'}, status=400)

        account1 = get_object_or_404(Account, id=account1_id)
        account2 = get_object_or_404(Account, id=account2_id)

        friend = get_object_or_404(Friend, account1=account1, account2=account2)
        friend.delete()
        return JsonResponse({'message': 'Friend removed'})

@csrf_exempt
def get_leaderboard(request):
    if request.method == "GET":
        mydata = Account.objects.all().order_by('-xp').values()[:10]
        return JsonResponse(list(mydata), safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class LikeListCreateView(generics.ListCreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

# class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

