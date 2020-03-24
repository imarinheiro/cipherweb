from django.shortcuts import render
from django.views.generic.edit import View
from rsa.report import set_context_key
from apprsa.forms.key_form import KeyForm


class KeyView(View):

    def get(self, request):
        form = KeyForm
        return render(request, 'apprsa/form.html', {'form': form})

    def post(self, request):
        form = KeyForm(request.POST)
        if form.is_valid():
            p_number = form.cleaned_data.get('p_number', 0)
            q_number = form.cleaned_data.get('q_number', 0)
            context = set_context_key(p_number, q_number)
            return render(request, 'apprsa/report_key.html', context)
        return render(request, 'apprsa/form.html', {'form': form})
