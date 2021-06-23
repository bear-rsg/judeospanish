from django.views.generic import CreateView, ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from . import models
from . import forms


class StoryCreateView(CreateView):
    """
    Class-based view to show the 'share your story' template
    """
    template_name = 'researchdata/story-create.html'
    form_class = forms.StoryCreateForm
    success_url = reverse_lazy('story-create-success')


class StoryCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the story create success template
    """
    template_name = 'researchdata/story-create-success.html'


class StoryDetailView(DetailView):
    """
    Class-based view to show the story detail template
    """
    template_name = 'researchdata/story-detail.html'
    queryset = models.Story.objects.filter(admin_published=True)


class StoryListView(ListView):
    """
    Class-based view to show the story list template
    Stories are grouped by location, which is why model = Location
    """
    template_name = 'researchdata/story-list.html'
    model = models.Location


class ParticipantCreateView(CreateView):
    """
    Class-based view to show the 'share your participant' template
    """
    template_name = 'researchdata/participant-create.html'
    form_class = forms.ParticipantCreateForm
    success_url = reverse_lazy('participant-create-success')


class ParticipantCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the participant create success template
    """
    template_name = 'researchdata/participant-create-success.html'
