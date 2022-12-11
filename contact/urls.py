from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('message/', views.message),
    path('subscribe', views.subscribe)
]
