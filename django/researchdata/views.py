from django.views.generic import CreateView, ListView
from . import models


class StoryCreateView(CreateView):
    """
    Class-based view to show the 'share your story' template
    """
    template_name = 'researchdata/story-create.html'
    model = models.Story
    fields = ('description',)


class StoryListView(ListView):
    """
    Class-based view to show the story list template
    Stories are grouped by location, which is why model = Location
    """
    template_name = 'researchdata/story-list.html'
    model = models.Location
