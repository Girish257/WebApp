from django.shortcuts import render
from django.conf import settings
from django. contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'app/index.html')

def abc(request):

    if request.method == 'POST':
        subject = request.POST.get('name')
        message = f'Hi , thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['girish.test1t111@gmail.com' ]
        # email_from = [request.POST.get('email')]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse("done")
    else:
        return render(request, 'app/enquiry.html', {})