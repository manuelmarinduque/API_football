from django.urls import path
from apps.apuesta import views

urlpatterns = [
#	path('apuesta/', views.ApuestaView.as_view(), name="signup"),
 	#path('signup/', SignUpView.as_view(), name="signup"),
 	path('apuesta/', views.apuesta_view, name="apuesta_view"),
 	path('apuestalista/', views.apuesta_list, name="apuesta_list")
 	#path('apuesta/', views.index, name="index"),
]
