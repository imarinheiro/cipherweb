from django.shortcuts import render
from django.views.generic.edit import View
from rsa.report import set_context_decrypt_number, set_context_decrypt_string
from apprsa.forms.decrypt_form import DecryptForm


class DecryptView(View):

    def get(self, request):
        form = DecryptForm
        return render(request, 'apprsa/form.html', {'form': form})

    def post(self, request):
        form = DecryptForm(request.POST)
        if form.is_valid():
            context = {}
            message = form.cleaned_data.get('message', '')
            first_key = form.cleaned_data.get('first_key', 0)
            second_key = form.cleaned_data.get('second_key', 0)
            if message.isdigit():
                context = set_context_decrypt_number(int(message), first_key, second_key)
            if message.isalpha():
                context = set_context_decrypt_string(message, first_key, second_key)
            return render(request, 'apprsa/report_decrypt.html', context)
        return render(request, 'apprsa/form.html', {'form': form})
