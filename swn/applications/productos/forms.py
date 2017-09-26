# -*- coding: utf-8 -*-
from django import forms

from .models import Citation, ProductSolicitude

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
                    'placeholder': 'E-mail',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Celular/Telefono',
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
                    'placeholder': '¿En qué horarios podemos llamarlo?',
                }
            ),
            'day_atention': forms.TextInput(
                attrs={
                    'placeholder': '¿Que días podemos llamarlo?',
                }
            ),
            'messagge': forms.Textarea(
                attrs={
                    'placeholder': 'Déjenos un mensaje...',
                    'rows':'4',
                }
            ),
        }


class ProductSolicitudeForm(forms.ModelForm):
    """
    formulario para registrar solicitud de producto
    """

    class Meta:
        model = ProductSolicitude
        fields = (
            'email',
            'phone',
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Teléfono o Celular',
                }
            ),
        }
