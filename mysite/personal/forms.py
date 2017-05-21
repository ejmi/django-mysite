from django import forms

class ContactForm(forms.Form):
    contant_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True)
