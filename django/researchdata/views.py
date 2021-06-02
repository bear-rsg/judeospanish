from django.views.generic import CreateView, ListView, TemplateView
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


class StoryListView(ListView):
    """
    Class-based view to show the story list template
    Stories are grouped by location, which is why model = Location
    """
    template_name = 'researchdata/story-list.html'
    model = models.Location
