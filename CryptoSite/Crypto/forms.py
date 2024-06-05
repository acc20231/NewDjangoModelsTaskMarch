from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.db.models import fields
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Логин(username)", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name']
            labels = {
                'first_name': 'Имя',
                'last_name': 'Фамилия',
            }
            widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean(self):

        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

# class ProfileUserForm(forms.ModelForm):
#     username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name', 'last_name']
#         labels = {
#             'first_name': 'Имя',
#             'last_name': 'Фамилия',
#         }
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-input'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-input'}),
#         }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password(self):
        return self.initial["password1"]


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label="Логин",
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username', 'password',]