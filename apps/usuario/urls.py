from django.urls import path
from apps.usuario.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='Home')
]
