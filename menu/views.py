from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from menu.forms import MenuForm
from django.contrib import messages
from menu.models import Menu, Kategori


def index(request):
    kategori = Kategori.objects.all().values()
    menu = Menu.objects.all()
    context = {
        'title': 'MENU',
        'kategori': kategori,
        'menu':  menu
    }
    return render(request, 'menu.html', context)


def add(request):
    form = MenuForm()
    context = {
        'title': 'ADD MENU',
        'context': 'Tambah',
        'form': form,
        'linkform': 'add/'
    }
    if request.method == 'POST':
        formset = MenuForm(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(
                request, request.POST['nama'] + " sudah berhasil ditambahkan")
            return HttpResponseRedirect('/menu')

    return render(request, 'menu-form.html', context)


def edit(request, nama):
    getmenu = Menu.objects.filter(nama=nama).get()
    form = MenuForm(instance=getmenu)
    context = {
        'title': 'EDIT MENU',
        'context': 'Edit',
        'form': form,
        'linkform': 'edit/' + nama,
        'delete': True,
        'menu': getmenu
    }

    if request.method == 'POST':
        formset = MenuForm(request.POST, instance=getmenu)
        if formset.is_valid():
            formset.save()
            messages.success(
                request, request.POST['nama'] + " sudah berhasil diubah")
            return HttpResponseRedirect('/menu')

    return render(request, 'menu-form.html', context=context)


def delete(request):
    menu = Menu.objects.filter(nama=request.POST['nama']).get()
    menu.delete()
    messages.success(request, request.POST['nama'] + " sudah berhasil dihapus")
    return JsonResponse({
        'confirm': '200'
    })
