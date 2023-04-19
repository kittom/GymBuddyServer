from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/<int:pk>', views.AccountDetail.as_view()),
    path('exercises/<int:account>/', views.ExerciseList.as_view()),
    path('exercise/', views.ExerciseView.as_view()),
    path('workouts/', views.WorkoutCreate.as_view()), 
    path('workouts/<int:account>/', views.WorkoutList.as_view()), 
    path('exercises_by_workout/<int:workout_id>/', views.ExerciseByWorkoutView.as_view()),
    path('workout/<int:pk>', views.WorkoutDetail.as_view()),
    path('search/', views.search_accounts, name='search_accounts'),
    
    path('friend/request/', views.FriendRequest.as_view(), name='friend-request'),
    path('friends/<int:pk>/', views.FriendRetrieveUpdateDestroyView.as_view(), name='friend_retrieve_update_destroy'),
    path('friends/', views.FriendListCreateView().as_view(), name="all friends"),
    path('posts/', views.PostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post_retrieve_update_destroy'),
    path('likes/', views.LikeListCreateView.as_view(), name='like_list_create'),
    path('likes/<int:pk>/', views.LikeRetrieveUpdateDestroyView.as_view(), name='like_retrieve_update_destroy'),
]