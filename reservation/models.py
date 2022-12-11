from django.db import models

class Audiens(models.Model):
    kuantitas = models.CharField(verbose_name="audiens", max_length=50)

    def __str__(self):
        return self.kuantitas


class Ruangan(models.Model):
    ruangan = models.CharField(max_length=50)

    def __str__(self):
        return self.ruangan

class WaktuPemesanan(models.Model):
    waktu = models.CharField(verbose_name="Waktu Pemesanan", max_length=50)

    def __str__(self):
        return self.waktu

class Reservation(models.Model):
    nama = models.CharField(
        verbose_name='Nama Pemesan', max_length=100)
    email = models.EmailField(
        verbose_name='Email Pemesan', max_length=254)
    telepon = models.CharField(
        verbose_name='Telepon/WA', max_length=50)
    acara = models.CharField(max_length=100)
    tanggal_pemesanan = models.DateField(
        verbose_name='Tanggal Acara')
    waktu_pemesanan = models.ForeignKey(WaktuPemesanan, on_delete=models.CASCADE)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    audiens = models.ForeignKey(Audiens, on_delete=models.CASCADE)
    keterangan = models.TextField()
    konfirmasi = models.BooleanField(default=False)
    selesai = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama + self.acara + str(self.tanggal_pemesanan)
