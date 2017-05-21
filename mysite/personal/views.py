from django.shortcuts import render

from .forms  import ContactForm

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html')
