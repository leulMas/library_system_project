# users/forms.py
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Use this if you use Django's default user

class AdminUserCreationForm(UserCreationForm):
    secret_code = forms.CharField(
        max_length=100,
        required=True,
        label="Admin Secret Code",
        widget=forms.PasswordInput(attrs={'placeholder': 'Admin secret code'})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

    def clean_secret_code(self):
        secret_code = self.cleaned_data.get('secret_code')
        ADMIN_SECRET_CODE = "Password"  # Replace with your admin secret
        if secret_code != ADMIN_SECRET_CODE:
            raise forms.ValidationError(
                "The secret code you entered is incorrect. Please contact the admin."
            )
        return secret_code

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8 or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise forms.ValidationError(
                "Password too weak. Must be at least 8 characters including a symbol."
            )
        return password
