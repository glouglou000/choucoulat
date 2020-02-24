from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
    """Home template, principal template. Is made up of an access to the site and
    sections to present the project (eyes, face, head, hand, langage sections)."""

    return render(request, "Home.html")



def site_partenaire(request):
    return render(request, "site_partenaire.html")
