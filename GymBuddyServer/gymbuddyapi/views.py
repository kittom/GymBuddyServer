from .models import Account, Exercise
from .serializers import AccountSerializer, ExerciseSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import ExerciseSerializer


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
            file = serializer.validated_data['file']
            serializer.save(file=file)
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


