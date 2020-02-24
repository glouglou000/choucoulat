from django.shortcuts import render

# Create your views here.
def visualisation(request):
    return render(request, "visualisation.html")
