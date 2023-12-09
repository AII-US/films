

from django.shortcuts import render

# Create your views here.
def load_data(request):
    # Llama al método populate DB de utils.py y obtén las entidades de la base de datos para luego mostrarlo.
    return render(request, 'load_data.html.html', context={'message': 'Data loaded successfully.'})

def home(request):
    return render(request, 'home.html')