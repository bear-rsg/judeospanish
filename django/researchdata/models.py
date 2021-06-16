from django.conf import settings
from django.core.mail import send_mail
from django.db import models
import logging
import textwrap

from django.db.models.fields import CharField, EmailField

logger = logging.getLogger(__name__)


class DataUse(models.Model):
    """
    The ways in which collected data can be used by the research team
    """

    name = models.CharField(max_length=255)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


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


class Story(models.Model):
    """
    A Story that a member of public shares with the project
    """

    class KnowledgeOfJudeoSpanish(models.TextChoices):
        """
        Choices of levels of knowledge of Judeo-Spanish
        """
        NATIVE = 'NTV', "I learned Judeo-Spanish as a native/home language in childhood"
        LATER = 'LTR', "I learned Judeo-Spanish as a non-native language later in life"
        NEVER = 'NVR', "I don't know Judeo-Spanish"

    description = models.TextField()
    image = models.ImageField(upload_to='researchdata/letters', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_url_embed = models.URLField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    location_other = models.CharField(max_length=255, blank=True, null=True)
    knowledge_of_judeospanish = models.CharField(max_length=3,
                                                 choices=KnowledgeOfJudeoSpanish.choices,
                                                 blank=True,
                                                 null=True)
    languages = models.ManyToManyField(Language, related_name="story", blank=True)
    data_use_agreements = models.ManyToManyField(DataUse, related_name="story", blank=True)

    # Author info
    author_name = CharField(max_length=100, blank=True, null=True)
    author_email = EmailField(blank=True, null=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=False)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        if self.location:
            return f"A story from {self.location}: {textwrap.shorten(self.description, width=40, placeholder='...')}"
        return f"A story: {textwrap.shorten(self.description, width=40, placeholder='...')}"

    def save(self, *args, **kwargs):
        """
        When a new model is saved:
        - email the research team
        - convert YouTube link
        """

        # If this is a new answer
        if self.meta_created_datetime is None:
            # Send email alert to research team
            try:
                send_mail("Grammars of Judeo-Spanish website: New story",
                          "A new story has been submitted.",
                          settings.DEFAULT_FROM_EMAIL,
                          settings.NOTIFICATION_EMAIL,
                          fail_silently=True)
            except Exception:
                logger.exception("Failed to send email")

        # Convert YouTube URLs to be suitable for embedding
        if self.video_url:
            self.video_url_embed = str(self.video_url).replace("/watch?v=", "/embed/")

        # Save new object
        super().save(*args, **kwargs)
