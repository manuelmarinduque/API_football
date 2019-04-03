from django.urls import path
from apps.usuario.views import SignUpView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='perfil')
]
