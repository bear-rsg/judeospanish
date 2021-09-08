from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3
from django.utils.translation import ugettext_lazy as _


class StoryCreateForm(forms.ModelForm):
    """
    A form for users to submit a 'Story'
    """

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 7}),
                                  label=_('Story text'))
    video_url = forms.URLField(label=_('YouTube video link'),
                               help_text=_('e.g. https://youtube.com/examplevideo. \
                                            Please remember to allow embedding permissions on your video.'),
                               required=False)
    audio_player_embed_code = forms.CharField(label=_('SoundCloud audio embed code'),
                                              help_text=_('e.g. Go to your SoundCloud audio file page, click Share, then click Embed, \
                                              and then copy and paste the contents of the Code box here'),
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
    data_use_agreements = forms.ModelMultipleChoiceField(label=_("I agree to the publication of my story \
                                                                  (recording and/or text and/or image) \
                                                                  in the following ways:"),
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
                  'audio_player_embed_code',
                  'location',
                  'location_other',
                  'knowledge_of_judeospanish',
                  'languages',
                  'author_name',
                  'author_email',
                  'data_use_agreements')


class ParticipantCreateForm(forms.ModelForm):
    """
    A form for users to volunteer as a 'Participant'
    """

    name = forms.CharField(label=_('Name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)
    location_birth_other = forms.CharField(label=_('Location of birth (if not available above)'),
                                           required=False)
    location_current_other = forms.CharField(label=_('Current location (if not available above)'),
                                             required=False)
    knowledge_of_judeospanish = forms.ChoiceField(choices=models.Story.KnowledgeOfJudeoSpanish.choices,
                                                  label=_('Knowledge of Judeo-Spanish'))
    name_of_judeospanish = forms.CharField(label=_('By what name(s) do you call Judeo-Spanish?'),
                                           help_text='e.g. ladino, djudezmo, djudeoespanyol, djudeoespañol, haketiya',
                                           required=False)
    languages = forms.ModelMultipleChoiceField(label=_('Languages known'),
                                               queryset=models.Language.objects,
                                               widget=forms.CheckboxSelectMultiple,
                                               help_text=_('Select all that apply'),
                                               required=False)
    languages_other = forms.CharField(label=_('Languages known (if not available above)'),
                                      required=False)
    participation_activities = forms.ModelMultipleChoiceField(label=_("I'm interested in participating in"),
                                                              queryset=models.ParticipationActivity.objects,
                                                              widget=forms.CheckboxSelectMultiple,
                                                              help_text=_('Select all that apply'),
                                                              required=False)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label=_('Any other comments'), required=False)

    # Google ReCaptcha
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Participant
        fields = ('name',
                  'email',
                  'location_birth',
                  'location_birth_other',
                  'location_current',
                  'location_current_other',
                  'knowledge_of_judeospanish',
                  'name_of_judeospanish',
                  'languages',
                  'languages_other',
                  'participation_activities',
                  'comments')
