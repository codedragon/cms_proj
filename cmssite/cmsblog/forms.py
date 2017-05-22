from django import forms
from cmsblog.models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # fields = ('title', 'text', 'category')
        # Unknown field(s) (category) specified for Post


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description',)


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'event_time',)
