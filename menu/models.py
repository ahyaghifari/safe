from django.db import models


class Kategori(models.Model):
    nama = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama


class Menu(models.Model):
    nama = models.CharField(max_length=100, unique=True)
    gambar = models.URLField()
    deskripsi = models.TextField(null=True)
    harga = models.SmallIntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
