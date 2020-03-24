from django.shortcuts import render
from django.views.generic.edit import View
from rsa.report import set_context_encrypt_number, set_context_encrypt_string

from apprsa.forms.encrypt_form import EncryptForm


class EncryptView(View):

    def get(self, request):
        form = EncryptForm
        return render(request, 'apprsa/form.html', {'form': form})

    def post(self, request):
        form = EncryptForm(request.POST)
        if form.is_valid():
            is_text = form.cleaned_data.get('is_text', False)
            message = form.cleaned_data.get('message', '')
            first_key = form.cleaned_data.get('first_key', 0)
            second_key = form.cleaned_data.get('second_key', 0)
            if is_text:
                context = set_context_encrypt_string(message, first_key, second_key)
            else:
                context = set_context_encrypt_number(int(message), first_key, second_key)
            return render(request, 'apprsa/report_encrypt.html', context)
        return render(request, 'apprsa/form.html', {'form': form})
