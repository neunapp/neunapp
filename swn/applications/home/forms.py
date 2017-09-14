from django import forms

from .models import Suscription


class SuscriptionForm(forms.ModelForm):
    """
    formulario para agregar citaciones
    """

    class Meta:
        model = Suscription
        fields = (
            'email',
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class':'suscription__form__input',
                    'placeholder': 'Correo Electronico',
                }
            ),
        }
