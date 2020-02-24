from django.shortcuts import render

#from .app.paths import 

# Create your views here.
def visualisation(request):

    if request.method == 'POST':

        start = request.POST.get('start')
        print(start)

    return render(request, "visualisation.html")
