from django import forms

from .validators import password_match_validator

#TODO: Add new form validators.

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthdate = forms.DateField(widget=forms.DateInput())
    username = forms.CharField(min_length=6)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(forms.Form, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        password_match_validator(password1, password2)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class NewPostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)

