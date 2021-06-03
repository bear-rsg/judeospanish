from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoryListView.as_view(), name='story-list'),
    path('<int:pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    path('create/', views.StoryCreateView.as_view(), name='story-create'),
    path('create/success/', views.StoryCreateSuccessTemplateView.as_view(), name='story-create-success'),
]
