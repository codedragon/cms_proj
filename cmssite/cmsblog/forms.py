from django import forms
from cmsblog.models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description', )


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'event_start', 'event_end', 'talks',)  # 'venue')


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ('name', 'bio',)


class TalkForm(forms.ModelForm):

    class Meta:
        model = Talk
        fields = ('title', 'abstract', )