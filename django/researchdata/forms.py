from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3


class StoryCreateForm(forms.ModelForm):
    """
    Form to specify fields in the story create form
    """

    description = forms.CharField(widget=forms.Textarea(),
                                  label='Share your story')
    video_url = forms.URLField(label='YouTube video link',
                               help_text='e.g. https://youtube.com/examplevideo')
    location_other = forms.CharField(label='Location (if not available above)')
    knowledge_of_judeospanish = forms.CharField(label='Knowledge of Judeo-Spanish')
    languages = forms.ModelMultipleChoiceField(label='Languages known',
                                               queryset=models.Language.objects,
                                               widget=forms.CheckboxSelectMultiple,
                                               help_text='Select all that apply')

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
