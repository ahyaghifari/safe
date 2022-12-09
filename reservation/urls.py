from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='reservation'),
    path('cek', views.cek),
    path('order', views.order, name='order-reservation')
]
