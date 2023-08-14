from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password')

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        email_check = User.objects.filter(email=email)
        if email_check.exists():
            raise forms.ValidationError('This Email already exists')
        if len(password) < 5:
            raise forms.ValidationError('Your password should have more than 5 characters')
        return super(UserRegisterForm, self).clean(*args, **kwargs)