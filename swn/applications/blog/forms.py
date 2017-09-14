from django import forms
from django import forms

from .models import Commentary

class SearchForm(forms.Form):
   '''
   formulario para buscar notas
   '''

   kword = forms.CharField(
       max_length='300',
       required=False,
       widget=forms.TextInput(
           attrs={
                'class':'blog-form__input',
                'placeholder': 'Buscar'
           }
       )
   )



class ComentarybyBlogForm(forms.ModelForm):
    """
    formulario para agregar comentarios a los temas del blog
    """

    class Meta:
        model = Commentary
        fields = (
            'email',
            'nick',
            'description',
        )
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'email',
                }
            ),
            'nick': forms.TextInput(
                attrs={
                    'placeholder': 'nickname',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'descripcion',
                }
            ),
        }
