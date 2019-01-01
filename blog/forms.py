from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.forms import (
    Form, CharField, Textarea, PasswordInput, ChoiceField, DateField,EmailField,
    ImageField,TextInput
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)





class UserLogin(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
