
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
            'day_atention',
            'messagge'
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Correo electronico',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefonos',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Direccion',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre o Empresa',
                }
            ),
            'hour_atention': forms.TextInput(
                attrs={
                    'placeholder': 'En que horarios podemos llamarlo',
                }
            ),
            'day_atention': forms.TextInput(
                attrs={
                    'placeholder': 'Que dias podemos llamarlo',
                }
            ),
            'messagge': forms.Textarea(
                attrs={
                    'placeholder': 'Dejenos un mensaje...',
                    'rows':'4',
                }
            ),
        }
