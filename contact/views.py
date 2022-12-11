from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from contact.forms import ContactForm
from contact.models import Contact, Subscriber
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages

def index(request):
    return render(request, 'kontak.html', {'title': 'KONTAK', 'form':ContactForm()})

def message(request):
    formset = ContactForm(request.POST)
    if formset.is_valid:
        formset.save()
        messages.success(request, "Pesan mu sudah diterima, terima kasih :) - ahyaghifari")
        return HttpResponseRedirect('/kontak')


def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({
                'responses' : '400',
                'message' : email + ' kamu sudah terdaftar'
            })
        else:
            byte_email = urlsafe_base64_encode(str(email).encode('utf-8'))
            link = "/kontak/unsubscribe/" + byte_email

            html = render_to_string('mail/subscribe.html', {'unsubscribe' : link})
            text = strip_tags(html)

            sendemail = EmailMultiAlternatives(
                "SUBSCRIBE SAFE",
                text,
                settings.EMAIL_HOST_USER,
                [email]
            )   

            sendemail.attach_alternative(html, "text/html")
            sendemail.send()
            Subscriber(email=email).save()
            return JsonResponse({
                'responses' : '200',
                'message' : 'Kamu berhasil mendaftar. Silahkan cek email kamu ' + email
            })