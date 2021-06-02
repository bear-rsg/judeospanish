from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3
from django.utils.translation import ugettext_lazy as _


class StoryCreateForm(forms.ModelForm):
    """
    Form to specify fields in the story create form
    """

    description = forms.CharField(widget=forms.Textarea(),
                                  label=_('Share your story'))
    video_url = forms.URLField(label=_('YouTube video link'),
                               help_text=_('e.g. https://youtube.com/examplevideo'))
    location_other = forms.CharField(label=_('Location (if not available above)'))
    knowledge_of_judeospanish = forms.CharField(label=_('Knowledge of Judeo-Spanish'))
    languages = forms.ModelMultipleChoiceField(label=_('Languages known'),
                                               queryset=models.Language.objects,
                                               widget=forms.CheckboxSelectMultiple,
                                               help_text=_('Select all that apply'))

    # Google ReCaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Story
        fields = ('description',
                  'image',
                  'video_url',
                  'location',
                  'location_other',
                  'knowledge_of_judeospanish',
                  'languages')
