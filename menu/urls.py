from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('add/', views.add, name='addmenu'),
    path('edit/<str:nama>', views.edit, name='editmenu'),
    path('delete/', views.delete, name='deletemenu'),
]
