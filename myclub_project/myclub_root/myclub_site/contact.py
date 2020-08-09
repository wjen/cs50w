from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection


class ContactForm(forms.Form):
    #  If you don’t specify the label attribute, Django uses the field name for the field label.
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label="Your Email Address")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # assert False, Using the assert False statement allows us to check the contents of the submitted form.
            # assert False
            con = get_connection(
                'django.core.mail.backends.console.EmailBackend'
            )
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact/contact.html', {
        'form': form, 'submitted': submitted
    })
