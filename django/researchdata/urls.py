from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.StoryCreateView.as_view(), name='story-create'),
    path('map/', views.StoryListView.as_view(), name='story-list'),
]
