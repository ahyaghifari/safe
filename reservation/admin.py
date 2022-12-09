from django.contrib import admin
from reservation.models import Reservation, Audiens, Ruangan
# Register your models here.

admin.site.register(Audiens)
admin.site.register(Ruangan)
admin.site.register(Reservation)