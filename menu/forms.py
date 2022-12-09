from django.forms import ModelForm
from menu.models import Menu


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        exclude = []
