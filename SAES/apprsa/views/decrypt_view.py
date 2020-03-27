from django.shortcuts import render
from django.views.generic.edit import View
from rsa.report import set_context_decrypt_number, set_context_decrypt_string
from apprsa.forms.decrypt_form import DecryptForm


class DecryptView(View):

    def get(self, request, **kwargs):
        form = DecryptForm(initial=kwargs)
        return render(request, 'apprsa/form.html', {'form': form})

    def post(self, request, **kwargs):
        form = DecryptForm(request.POST)
        if form.is_valid():
            is_text = form.cleaned_data.get('is_text', False)
            message = form.cleaned_data.get('message', 0)
            first_key = form.cleaned_data.get('first_key', 0)
            second_key = form.cleaned_data.get('second_key', 0)
            if is_text:
                context = set_context_decrypt_string(int(message), first_key, second_key)
                context['is_text'] = is_text
            else:
                context = set_context_decrypt_number(int(message), first_key, second_key)
                context['is_text'] = is_text
            return render(request, 'apprsa/report_decrypt.html', context)
        return render(request, 'apprsa/form.html', {'form': form})
