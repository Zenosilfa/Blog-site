from django import forms
from click import confirm


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı: ")
    password = forms.CharField(max_length=50,label="Şifre: ",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label="Şifreni Onayla: ",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolan eşleşmiyor...")

       
        values = {
            "username" : username,
            "password" : password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı: ")
    password = forms.CharField(label="Parola: ",widget=forms.PasswordInput)