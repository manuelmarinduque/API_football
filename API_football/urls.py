"""API_football URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from API_football.views import HomePageView, UsuarioList, SaldoUpdate, UsuarioDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='Home'),
    # Paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.usuario.urls')),
    path('partidos/', include('apps.partido.urls')),
    path('listado/', UsuarioList.as_view(), name='listado'),
    path('listado/detail/<int:pk>/', UsuarioDetailView.as_view(), name='listado_detail'),
    path('listado/detail/actualizar/<int:pk>/', SaldoUpdate.as_view(), name='actu_saldo'),
    path('apuestas/', include('apps.apuesta.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
