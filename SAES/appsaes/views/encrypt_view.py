from django.shortcuts import render
from django.views.generic.edit import View
from appsaes.forms.form import TextForm
from s_aes.report_generate import set_context_encrypt


class EncryptView(View):

    def get(self, request):
        form = TextForm
        return render(request, 'appsaes/form.html', {'form': form})

    def post(self, request):
        form = TextForm(request.POST)
        if form.is_valid():
            context = set_context_encrypt(form.cleaned_data['text'], form.cleaned_data['key'])
            return render(request, 'appsaes/report_encrypt.html', context)
        return render(request, 'appsaes/form.html', {'form': form})
