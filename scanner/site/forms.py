
from django import forms

class SSHBruteforceForm(forms.Form):

    username = forms.CharField(min_length=3, label="Username", required=True, initial="")
    password = forms.CharField(min_length=3, label="Password", required=True, initial="")
