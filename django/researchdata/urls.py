from django.urls import path
from . import views

urlpatterns = [
    # Story
    path('stories/',
         views.StoryListView.as_view(),
         name='story-list'),
    path('stories/<int:pk>/',
         views.StoryDetailView.as_view(),
         name='story-detail'),
    path('stories/create/',
         views.StoryCreateView.as_view(),
         name='story-create'),
    path('stories/create/success/',
         views.StoryCreateSuccessTemplateView.as_view(),
         name='story-create-success'),
    # Participant
    path('participant/',
         views.ParticipantCreateView.as_view(),
         name='participant-create'),
    path('participant/success/',
         views.ParticipantCreateSuccessTemplateView.as_view(),
         name='participant-create-success'),
]
