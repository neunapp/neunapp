
from django import forms

from .models import Citation

class CitationForm(forms.ModelForm):
    """ 
    formulario para agregar citaciones
    """

    class Meta:
        model = Citation
        fields = (
            'email',
            'phone',
            'address',
            'name',
            'hour_atention',
            'day_atention'
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'correo',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'telefono',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'direccion',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'nombre',
                }
            ),
            'hour_atention': forms.TextInput(
                attrs={
                    'placeholder': 'hora de atencion',
                }
            ),
            'day_atention': forms.TextInput(
                attrs={
                    'placeholder': 'dia de atencion',
                }
            ),
        }






