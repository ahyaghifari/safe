from django.db import models

# Create your models here.

class Contact(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pesan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama + self.email
    

class Subscriber(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    