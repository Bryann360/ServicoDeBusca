from django import forms
from .models import Produto, Esqueleto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'descricao', 'imagem', 'foto']
        widgets = {
            'titulo': forms.HiddenInput(),
            'descricao': forms.HiddenInput(),
            'imagem': forms.HiddenInput(),
            'foto': forms.HiddenInput(),
        }


