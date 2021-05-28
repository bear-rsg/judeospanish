from django.db import models
import textwrap


class Language(models.Model):
    """
    The language(s) that a user knows
    """

    name = models.CharField(max_length=150)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    The locations of the people who submit a story
    """

    name = models.CharField(max_length=150)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class NativeSpeaker(models.Model):
    """
    Whether the user is a native speaker of Judeo Spanish or not
    """

    name = models.CharField(max_length=150)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    """
    A Story that a member of public shares with the project
    """

    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='researchdata/letters', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    location_other = models.CharField(max_length=255, blank=True, null=True)
    native_speaker = models.ForeignKey(NativeSpeaker, on_delete=models.SET_NULL, blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name="story", blank=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

    # Metadata fields
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    meta_firstpublished_datetime = models.DateTimeField(blank=True, null=True, verbose_name="First Published")

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        if self.location:
            return f"A story from {self.location}: {textwrap.shorten(self.description, width=40, placeholder='...')}"
