from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='reservation'),
    path('all/', views.all, name='reservasi-all'),
    path('detail/<str:id>', views.detail, name="reservation-detail"),

    path('cek', views.cek),

    #CURD

    path('order', views.order, name='order-reservation'),
    path('edit/<str:id>', views.edit, name='reservation-edit'),
    path('delete/', views.delete)
]
