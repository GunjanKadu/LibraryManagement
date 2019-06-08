from django import forms
from django.contrib.auth.models import User
from Library_App.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The Passwords You Entered Do Not Match")

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
