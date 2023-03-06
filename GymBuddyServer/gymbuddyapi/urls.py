from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/<int:pk>', views.AccountDetail.as_view()),
    # path('exercises/', views.ExercisetList.as_view()),
    # path('exercise/<int:pk>', views.ExerciseDetail.as_view()),    
]