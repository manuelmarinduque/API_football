from django.urls import path
from apps.usuario.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
]
