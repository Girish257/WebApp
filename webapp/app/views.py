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
        message = f'Hi, User'
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['girish.test1g@gmail.com' ]

        # email_from1 = [request.POST.get('email')]
        send_mail( subject, message, email_from, recipient_list )


        message1 = f'ADMIN'
        recipient_list1 = ['girish.test1t@gmail.com' ]

        send_mail( subject, message1, email_from, recipient_list1 )
        return render(request ,'app/thankyou.html')
    else:
        return render(request, 'app/enquiry.html', {})
    
def new(request):
    return render(request, 'app/new.html')

def two(request):
    return render(request, 'app/two.html')