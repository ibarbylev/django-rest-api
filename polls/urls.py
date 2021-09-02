from django.contrib import admin
from django.urls import path, include

# from polls import views
from polls import apiviews
urlpatterns = [
    # path('polls/', views.polls_list, name='polls_list'),
    # path('polls/<int:pk>/', views.polls_detail, name='polls_detail'),
    # path('choices/', views.choices_list, name='choices_list'),
    # path('choices/<int:pk>/', views.choices_detail, name='choices_detail'),
    path('polls/', apiviews.PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', apiviews.PollDetail.as_view(), name='polls_detail'),
    path("polls/<int:pk>/choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", apiviews.CreateVote.as_view(), name="create_vote"),
]
