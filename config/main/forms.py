from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Required')
    send_emails = forms.BooleanField(required=False)
    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        user = save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user