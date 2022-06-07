from django.shortcuts import render, redirect
from .forms import KutubxonaForm
from django.views.generic import View
from django.contrib import messages
from .models import Kutubxona

# Create your views here.


class KutubIndex(View):
    def get(self, request):
        form = KutubxonaForm()
        return render(request, 'kutub/index.html', {
            'form': form,
            'list': Kutubxona.objects.all()
        })

    def post(self, request):
        form = KutubxonaForm(data=request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "OK")

            return redirect('kutub:index')

        return render(request, 'kutub/index.html', {
            'form': form
        })
