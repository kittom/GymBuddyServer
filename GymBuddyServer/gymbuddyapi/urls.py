from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/<int:pk>', views.AccountDetail.as_view()),
    path('exercises/<int:account>/', views.ExerciseList.as_view()),
    path('exercise/', views.ExerciseView.as_view()),    
]