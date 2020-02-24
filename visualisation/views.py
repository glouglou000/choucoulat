import os


from django.shortcuts import render
from .paths import upload_folder, upload_video

#from .app.paths import 

# Create your views here.
def visualisation(request):


    username = request.user
    path_user = upload_folder + "/" + str(username)
    user_list = os.listdir(path_user)

    
    liste_path = [upload_video.format(username, i) for i in user_list]

    context = {"video_user": liste_path}

    return render(request, "visualisation.html", context)
