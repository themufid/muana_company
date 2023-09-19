from django.urls import path, include
from .views import beranda_view, masuk_view, daftar_view
from .views import presensi_view
from .views import pendaftaran_view
from .views import modul_view
from .views import laporan_view
from .views import about_view
from .views import articles_view
from .views import contact_view
from .views import daftar_view
from .views import disclaimer_view
from .views import index_view
from .views import privacy_view
from .views import service_view
from .views import term_view
from .views import keluar_view
from .views import jadwal_view

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('beranda/', beranda_view, name='beranda'),
    path('daftar/', daftar_view, name='daftar'),
    path('masuk/', masuk_view, name='masuk'),
    path('keluar/', keluar_view, name='keluar'),
    path('presensi/', presensi_view, name='presensi'),
    path('pendaftaran/', pendaftaran_view, name='pendaftaran'),
    path('modul/', modul_view, name='modul'),
    path('laporan/', laporan_view, name='laporan'),
    path('about/', about_view, name='about'),
    path('articles/', articles_view, name='articles'),
    path('contact/', contact_view, name='contact'),
    path('daftar/', daftar_view, name='daftar'),
    path('disclaimer/', disclaimer_view, name='disclaimer'),
    path('index', index_view, name='index'),
    path('privacy-policy/', privacy_view, name='privacy-policy'),
    path('service/', service_view, name='service'),
    path('term/', term_view, name='term'),
    path('jadwal/', jadwal_view, name='jadwal'),
]

