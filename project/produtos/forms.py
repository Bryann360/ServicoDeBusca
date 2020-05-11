from django import forms
from .models import Produto, Esqueleto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }
