from django import forms
from .models import Author
from django.contrib.auth.models import User


class AuthorForm(forms.ModelForm):
    password = forms.CharField(label="Please, type your password", widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label="Please, repeat your password", widget=forms.PasswordInput(render_value=False))
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "email",
            "avatar",
        ]

    def clean_email(self):

        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("This email is used")

    def clean(self):
        cleaned_data = super(AuthorForm, self).clean()
        if 'password' in cleaned_data and 'password1' in cleaned_data\
                and cleaned_data['password'] != cleaned_data['password1']:
            raise forms.ValidationError("The password does not match ")
        return cleaned_data


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Author
        fields = [
            'email',
        ]
