from django.shortcuts import render

# Create your views here.

def compte(request):
    return render(request, "compte.html")
