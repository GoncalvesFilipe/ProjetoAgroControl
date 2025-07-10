from django import forms
from .models import Venda, ItemVenda
from django.forms.models import inlineformset_factory

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['funcionario']

# Formset para adicionar vários itens na mesma venda
ItemVendaFormSet = inlineformset_factory(
    Venda,
    ItemVenda,
    fields=['produto', 'quantidade', 'preco_unitario'],
    extra=1,
    can_delete=True
)