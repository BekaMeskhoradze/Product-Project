from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(
        max_length=9,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '+9955XX XXX XXX'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'phone', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone