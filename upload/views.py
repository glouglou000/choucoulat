from django.shortcuts import render

# Create your views here.
def telechargement(request):
    return render(request, "telechargement.html")
