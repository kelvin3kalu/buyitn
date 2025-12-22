# forms.py
from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



class MakeAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

