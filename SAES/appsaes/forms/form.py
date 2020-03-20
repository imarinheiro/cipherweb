from django import forms


class TextForm(forms.Form):
    text = forms.IntegerField(label='Texto', required=True, max_value=999999999999999999999999999999999999)
    key = forms.IntegerField(label='Chave', required=True, max_value=65535)

