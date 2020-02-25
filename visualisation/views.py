import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os. getcwd()
path_current = os.path.basename(path)


from django.shortcuts import render
from .paths import *



from .app.paths import dlib_model, eyes_image, blink_image



from .app.pre_treatment.pre_test import search_video_size
from .app.pre_treatment.writter import video_writter

from .app.recuperate_points.face_points import load_model_dlib
from .app.video_capture_to_face_APP_2 import video_capture_to_face


def visualisation(request):

    if request.method == 'POST':

        username = request.user
        video = request.POST.get('video')

        video_path_media = BASE_DIR + "/" + video

        predictor, detector = load_model_dlib(dlib_model)
 
        video_size = search_video_size(video_path_media, predictor, detector, dlib_model)
        print(video_size)

        video_capture_to_face(video_path_media, video, eyes_image,
                              blink_image, username, video_size)


    else:

        username = request.user
        path_user = upload_folder + "/" + str(username)
        user_list = os.listdir(path_user)

        liste_path = [upload_video.format(username, i) for i in user_list]

        context = {"video_user": liste_path}

        return render(request, "visualisation.html", context)
