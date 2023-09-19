from django import forms
from .models import Presensi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Jadwal

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class DaftarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class MasukForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = ['nama_siswa', 'tanggal', 'hadir', 'tutor']

class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['hari', 'jam_pelajaran', 'mata_pelajaran', 'kelas']