from django import forms
from django.utils.safestring import mark_safe

class LoginForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Your password", widget=forms.PasswordInput(),max_length=100)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Your password", widget=forms.PasswordInput(),max_length=100)
    repassword = forms.CharField(label="Repit password", widget=forms.PasswordInput(),max_length=100)


class BooksForm(forms.Form):
    bookname = forms.CharField(label="Book Name", max_length=100)
    context = forms.CharField(label="Context", max_length=100)
    editorial = forms.CharField(label="Editorial", max_length=100)
    paginas = forms.CharField(label="Number of Pages", max_length=100)
    picture = forms.CharField(label="Picture", max_length=100)

