from django.conf import settings
from django.shortcuts import render
from reservation.forms import ReservationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from reservation.models import Reservation
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from django.contrib import messages


def index(request):
    context = {
        'title': 'RESERVASI',
        'form': ReservationForm()
    }
    return render(request, 'reservation.html', context)


def order(request):
    formset = ReservationForm(request.POST)
    context = {
        'name': request.POST['nama'],
        'wa': request.POST['telepon'],
        'date': request.POST['tanggal_pemesanan'],
        'time': request.POST['waktu_pemesanan'],
        'created': datetime.now(),
        # 'until': datetime.now() + timedelta(hours=1)
    }
    tmp = render_to_string(
        'mail/reservation-confirmation.html', context)
    pln_tmp = strip_tags(tmp)

    if formset.is_valid():
        formset.save()
        send_mail("Reservation Confirmation", '',
                  settings.EMAIL_HOST_USER, [request.POST['email']], html_message=tmp)
        messages.success(request, "Reservasi mu kami sudah terima, silahkan cek emailmu " +
                         request.POST['email'] + " untuk konfirmasi ")
        return HttpResponseRedirect('/reservasi')


def cek(request):
    date = request.GET['date']

    if Reservation.objects.filter(tanggal_pemesanan=date).exists():
        return JsonResponse({
            'response': '400',
            'message': '*Maaf untuk tanggal ' + date + ' sudah tidak tersedia :('
        })
    else:
        return JsonResponse({
            'response': '200',
            'message': '*Ruang untuk tanggal ' + date + ' tersedia :)'
        })
