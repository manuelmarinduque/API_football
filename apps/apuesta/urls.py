from django.urls import path
from apps.apuesta import views

urlpatterns = [
#	path('apuesta/', views.ApuestaView.as_view(), name="signup"),
 	#path('signup/', SignUpView.as_view(), name="signup"),
 	path('apuesta/', views.apuesta_view, name="apuesta_view"),
 	#path('apuesta/', views.index, name="index"),
]
