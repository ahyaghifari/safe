from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from reservation.forms import ReservationForm, ReservationFormEdit
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from reservation.models import Reservation
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from django.contrib import messages
from datetime import datetime
from django.utils.formats import get_format
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    context = {
        'title': 'RESERVASI',
        'form': ReservationForm()
    }
    return render(request, 'reservation.html', context)

@staff_member_required
def all(request):
    reservasi = Reservation.objects.all()
    return render(request, 'reservation-all.html', {'title': "ALL RESERVATION", 'reservasi': reservasi})

def detail(request, id):
    # t = get_format(tanggal)
    context = {
        'title' : "RESERVATION DETAIL",
        'reservasi' : Reservation.objects.filter(id = id).get()
    }
    return render(request, 'reservation-detail.html', context)

# CRUD
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

@staff_member_required
def edit(request, id):
    getreservasi = Reservation.objects.filter(id=id).get()
    form = ReservationFormEdit(instance=getreservasi)

    if request.method == "POST":
        formset = ReservationFormEdit(request.POST, instance=getreservasi)
        if formset.is_valid:
            formset.save()
            messages.success(
                request, "Reservasi dari " + request.POST['nama'] + " pada tanggal "+ request.POST['tanggal_pemesanan'] + " sudah berhasil diubah")
            return HttpResponseRedirect(reverse('/reservasi/detail/' + id))

    return render(request, 'reservation-edit.html', {'title' : 'RESERVATION EDIT', 'form':form, 'id':id})

@staff_member_required
def delete(request):
    getreservasi = Reservation.objects.filter(id=request.POST['id']).get()
    getreservasi.delete()
    messages.success(request, "Reservasi sudah dihapus")
    return JsonResponse({
        'confirm' : '200'
    })


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
