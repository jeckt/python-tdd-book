from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse

from accounts.models import Token

SUBJECT = 'Your login link for Superlists'
EMAIL = 'noreply@superlists'

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = 'Use this link to log in:\n\n%s' % (url,)
    send_mail(SUBJECT,
              message_body,
              EMAIL,
              [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
