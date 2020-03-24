from django import forms
from rsa.util import transform_string_to_number

from apprsa.validators.validators import validate_message_length


class EncryptForm(forms.Form):
    message = forms.CharField(validators=[validate_message_length], label='Mensagem', required=True)
    first_key = forms.IntegerField(label='Chave (N)', required=True, min_value=0)
    second_key = forms.IntegerField(label='Chave (E)', required=True, min_value=0)
    is_text = forms.BooleanField(label='Criptografia de Texto', initial=False, required=False)

    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get("message")
        first_key = cleaned_data.get("first_key")

        if message and first_key:
            msg = "A chave deve ser maior para criptografar a mensagem."
            result = None
            if message.isdigit():
                result = int(message)
            if message.isalpha():
                result = transform_string_to_number(message)
            if result >= first_key:
                self.add_error('message', msg)
                self.add_error('first_key', msg)
