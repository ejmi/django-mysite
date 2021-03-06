from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms  import ContactForm


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    title = "Contact us"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.iteritems():
            #print key, value
        form_email = form.cleaned_data.get('contact_email')
        form_context = form.cleaned_data.get('content')
        form_name = form.cleaned_data.get('contact_name')
        subject = 'Hello!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youremail.com']
        contact_message = "%s: %s via %s"%(
                form_name,
                form_context,
                form_email)

        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)
        return redirect('contact')
    context = {
        'form': form,
        'title': title,
        'title_align_center': title_align_center,
    }
    return render(request, 'personal/contact.html', context)
