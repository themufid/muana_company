from django.db import models

class UserProfile(models.Model):
    nama = models.CharField(max_length=100)
    # Tambahkan field lain sesuai kebutuhan

class Testimoni(models.Model):
    nama = models.CharField(max_length=100)
    testimoni = models.TextField()
    
class Presensi(models.Model):
    nama_siswa = models.CharField(max_length=100)
    tanggal = models.DateField()
    hadir = models.BooleanField()
    tutor = models.CharField(max_length=100)
    
class Jadwal(models.Model):
    hari = models.CharField(max_length=100)
    jam_pelajaran = models.CharField(max_length=100)
    mata_pelajaran = models.CharField(max_length=100)
    kelas = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_siswa
    
class JadwalForm(models.Model):
    hari = models.CharField(max_length=255)
    jam_pelajaran = models.CharField(max_length=255)
    mata_pelajaran = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)

    def __str__(self):
        return self.mata_pelajaran
