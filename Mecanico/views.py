from django.shortcuts import render

# Create your views here.

def mecanico (request):
    return render(request, 'Mecanico/mecanico.html')