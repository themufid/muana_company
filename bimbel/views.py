from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import Jadwal
from .forms import JadwalForm

def daftar_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beranda')
    else:
        form = CustomUserCreationForm()

    return render(request, 'daftar.html', {'form': form})

def masuk_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username atau password salah')
        return render(request, 'beranda.html')
    return render(request, 'masuk.html')

@login_required
def keluar_view(request):
    logout(request)
    return redirect('masuk')

def beranda_view(request):
    return render(request, 'beranda.html')

def presensi_view(request):
    return render(request, 'presensi.html')

def modul_view(request):
    return render(request, 'modul.html')

def laporan_view(request):
    return render(request, 'laporan.html')

def pendaftaran_view(request):
    return render(request, 'pendaftaran.html')

def about_view(request):
    return render(request, 'about.html')

def articles_view(request):
    return render(request, 'articles.html')

def contact_view(request):
    return render(request, 'contact.html')

def daftar_view(request):
    return render(request, 'daftar.html')

def disclaimer_view(request):
    return render(request, 'disclaimer.html')

def index_view(request):
    return render(request, 'index.html')

def privacy_view(request):
    return render(request, 'privacy-policy.html')

def service_view(request):
    return render(request, 'service.html')

def term_view(request):
    return render(request, 'term.html')

def jadwal_view(request):
    return render(request, 'jadwal.html')

def pendaftaran(request):
    return render(request, 'pendaftaran.html')
