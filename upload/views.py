from django.shortcuts import render
from .models import video_upload
from .forms import video_upload_form



def uploading_file(request):
    """Here is a function for uploading files.
    We call the form, verif his validity, cleanning it, save it
    and return name of video for the next AJAX"""

    #Call form.
    form = video_upload_form(request.POST, request.FILES)

    #Post from template.²
    if request.method == 'POST':

        print("Uploading video.")

        #Verify validity of the form.
        if form.is_valid():

            print("Form uploading video is valid.")
            
            #Uploading file.
            name_video = request.FILES['docfile']                       #Recuperate the file.
            form.cleaned_data['docfile'].name                           #Cleanning.
            newdoc = video_upload(docfile = request.FILES['docfile'])   #Call model.
            newdoc.save()                                               #Saving.

            print("video name's : ", str(name_video))

            return JsonResponse({"video_name" : str(name_video)})


def telechargement(request):

    form = video_upload_form(request.POST, request.FILES)
    context = {"form": form}
    return render(request, "telechargement.html", context)
















