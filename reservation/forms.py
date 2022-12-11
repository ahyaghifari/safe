from django.forms import ModelForm, TextInput, RadioSelect, NumberInput, widgets
from reservation.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        # fields = '__all__'
        exclude = ["konfirmasi", "selesai"]
        widgets = {
            'tanggal_pemesanan': widgets.DateInput(attrs={'type': 'date'}),
        }

class ReservationFormEdit(ModelForm):
    class Meta:
        model = Reservation
        exclude = []