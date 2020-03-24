from django import forms

from apprsa.validators.validators import validate_is_prime


class KeyForm(forms.Form):
    p_number = forms.IntegerField(validators=[validate_is_prime],
                                  label='Número Primo (P)',
                                  required=True,
                                  min_value=0)
    q_number = forms.IntegerField(validators=[validate_is_prime],
                                  label='Número Primo (Q)',
                                  required=True,
                                  min_value=0)
