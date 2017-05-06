from django import forms
from cmsblog.models import Post, Category


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
