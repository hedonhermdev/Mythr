from django import forms
from .models import Post

class NewPostForm(forms.Form):
    title = forms.CharField(required=True)
    author = forms.CharField()
    content = forms.CharField(widget=forms.Textarea, required=True)


class CommentForm(forms.Form):
    content  = forms.CharField(widget=forms.Textarea, required=True)
    author = forms.CharField()

