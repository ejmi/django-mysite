from django.shortcuts import render

from .forms  import ContactForm

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    form_class = ContactForm
    return render(request, 'personal/contact.html', {'form': form_class,})
