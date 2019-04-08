from django import forms
from apps.apuesta.models import Apuesta



class ApuestaForm(forms.ModelForm):
    class Meta:
        model = Apuesta
        fields = [
            'idApuesta',
            'tipo',
            'fechaApuesta',
            'montoApuesta',
            'gano',
            'valorganado',
            'nombreEquipo',
            'idPartido',
            'golesLocal',
            'golesVisitante',
            'diferenciaGoles',
            'cedula',

        ]

    labels = {
        'idApuesta': 'IDApuesta',
        'tipo': 'Tipo',
        'fechaApuesta': 'Fecha Apuesta',
        'montoApuesta': 'Monto Apuesta',
        'gano': 'Gano',
        'valorganado': 'Valor Ganado',
        'nombreEquipo': 'Nombre Equipo',
        'idPartido': 'ID Partido',
        'golesLocal': 'Goles Local',
        'golesVisitante': 'Goles Visitante',
        'diferenciaGoles': 'Diferencia Goles',
        'cedula': 'Cedula',

    }

    CHOICES = (('GANADOR', 'MARCADOR', 'DIFERENCIA GOL'))

    widgets = {
        'idApuesta': forms.TextInput(attrs={'class': 'form-control'}),
        'tipo': forms.Select(choices = CHOICES),
        'fechaApuesta': forms.DateField(label='Fecha Apuesta:'),
        'montoApuesta': forms.TextInput(attrs={'class': 'form-control'}),
        'gano': forms.BooleanField(required=False),
        'valorganado': forms.TextInput(attrs={'class': 'form-control'}),
        'nombreEquipo': forms.TextInput(attrs={'class': 'form-control'}),
        'idPartido': forms.TextInput(attrs={'class': 'form-control'}),
        'golesLocal': forms.TextInput(attrs={'class': 'form-control'}),
        'golesVisitante': forms.TextInput(attrs={'class': 'form-control'}),
        'diferenciaGoles': forms.TextInput(attrs={'class': 'form-control'}),
        'cedula': forms.TextInput(attrs={'class': 'form-control'}),

    }
