from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

SUBJECT = 'Your login link for Superlists'
EMAIL = 'noreply@superlists'

def send_login_email(request):
    email = request.POST['email']
    send_mail(SUBJECT,
              'body text tbc',
              EMAIL,
              [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')
