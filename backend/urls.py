from django.contrib import admin
from django.urls import path, include
from bimbel.views import masuk_view
from bimbel.views import beranda_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('', beranda_view, name='beranda'),
    path('masuk', masuk_view, name='masuk'),
    path('bimbel/', include('bimbel.urls')),
]
