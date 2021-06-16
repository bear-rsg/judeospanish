from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3
from django.utils.translation import ugettext_lazy as _


class StoryCreateForm(forms.ModelForm):
    """
    A form for users to submit a 'Story'
    """

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}),
                                  label=_('Share your story'))
    video_url = forms.URLField(label=_('YouTube video link'),
                               help_text=_('e.g. https://youtube.com/examplevideo'),
                               required=False)
    location_other = forms.CharField(label=_('Location (if not available above)'),
                                     required=False)
    knowledge_of_judeospanish = forms.ChoiceField(choices=models.Story.KnowledgeOfJudeoSpanish.choices,
                                                  label=_('Knowledge of Judeo-Spanish'))
    languages = forms.ModelMultipleChoiceField(label=_('Languages known'),
                                               queryset=models.Language.objects,
                                               widget=forms.CheckboxSelectMultiple,
                                               help_text=_('Select all that apply'),
                                               required=False)
    author_name = forms.CharField(label=_('Name'),
                                  help_text=_('Optional. Your name will not be displayed on the website.'),
                                  required=False)
    author_email = forms.EmailField(label=_('Email'),
                                    help_text=_('Optional. Your email address will not be displayed on the website.'),
                                    required=False)
    data_use_agreements = forms.ModelMultipleChoiceField(label=_('I agree to my data being used for the following'),
                                                         queryset=models.DataUse.objects,
                                                         widget=forms.CheckboxSelectMultiple,
                                                         help_text=_('Select all that apply'),
                                                         required=False)

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
                  'languages',
                  'author_name',
                  'author_email',
                  'data_use_agreements')
