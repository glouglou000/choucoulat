"""From the MVT architecture, we are situate on the view.
It's the inteface beetween template and model (data base)"""

import os
import cv2
import time
from django.shortcuts import render

#Json response to template
from django.http import JsonResponse

#Protection
from django.views.decorators.csrf import csrf_protect

#Uploading model/form
from .models import video_upload
from .forms import video_upload_form

from .eyes_detector.video_capture_writte import video_capture_treament
from .eyes_detector.paths import media_path, dlib_model

from .eyes_detector.paths import path_data
from .eyes_detector.paths import path_data_video
from .eyes_detector.paths import blink_image
from .eyes_detector.paths import eyes_image
from .eyes_detector.paths import video_save_media


from .eyes_detector.video_capture_sleep_APP_1  import video_capture_to_face_sleep       #Face
from .eyes_detector.video_capture_to_face_APP_2 import video_capture_to_face            #sleep
from .eyes_detector.video_capture_eyes_position_APP_3 import recuperate_eyes_position   #web
#from .eyes_detector.video_capture_APP_4 import video_capture                            #All



def recuperate_data():

    start_time_data_list = time.time()

    data = os.listdir(path_data)
    data = sorted(data)
    number_file = len(data)

    print("Count file to treat : ", number_file)
    print("running data took : ", time.time() - start_time_data_list)

    return data


def recuperate_dimensions_video(video):

    #Recuperate dimensions of video.
    cap = cv2.VideoCapture(video)
    width_video  = int(cap.get(3))
    height_video = int(cap.get(4))

    return height_video, width_video


def eye_tracking():

    #Recuperate length and file.
    data = recuperate_data()

    #Run data.
    for video in data:
        video_path = path_data_video.format(video)

        print("\nin course: ", video)

        #Recuperate eye position
        paths = recuperate_eyes_position(video_path, video)

        print(paths)
        return paths

def all_application():

    #Recuperate length and file.
    data = recuperate_data()

    #Run data.
    for video in data:
        video = path_data_video.format(video)

        print("\nin course: ", video)

        #Recuperate eye position
        video_capture(video)


def sleeping():

    #Recuperate length and file.
    data = recuperate_data()

    #Run data.
    for video in data:
        video_path = path_data_video.format(video)

        print("\nin course: ", video)

        #Recuperate eye position
        report, video_name = video_capture_to_face_sleep(video_path, video)
        return report, video_name 

def face_animation():

    #Recuperate length and file.
    data = recuperate_data()

    #Run data.
    for video in data:
        video_path = path_data_video.format(video)

        print("\nin course: ", video)

        #Recuperate eye position
        path_save = video_capture_to_face(video_path, video, eyes_image, blink_image)
        return path_save


def delete_video_wrotte():
    pass

def to_database():
    pass


def application(request):

    if request.method == 'POST':

        application = request.POST.get('application')
        video_name  = request.POST.get('video_name')

        print(application)
        print(video_name)


        if application == "eyes_tracking" and video_name:
            paths = eye_tracking()
            video, track1, track2, p1, p2, p3, p4, p5, p6 = paths
            response = {"video":video, "tracking1": track1, "tracking2": track2,
                        "p1":p1, "p2":p2, "p3":p3, "p4":p4, "p5":p5, "p6":p6}

            print(response)

        elif application == "sleep" and video_name:
            report, video_name  = sleeping()
            response = {"video_situation":video_name, "report":report}

        elif application == "face" and video_name:
            print("Face application call ! ")
            path_save = face_animation()
            response = {"video_situation1":path_save[0],
                        "video_situation2":path_save[1]}

        elif application == "test" and video_name:
            all_application()
            response = {"video_situation":""}


        return JsonResponse(response)








def verify(request):
    """Here we call this function with ajax for now if we can send response,
    the respsons is a video part.
    If chargement is egal to 3 we can send video (3 videos are writte.)."""

    if request.method == 'POST':
        verification = request.POST.get('verification')
        if verification == "verification":

            liste = os.listdir(path_data)

            counter = 0
            for i in liste:

                video_name = path_data_video.format(i)

                cap = cv2.VideoCapture(video_name)
                number_picture = cap.get(cv2.CAP_PROP_FRAME_COUNT)

                if number_picture > 0:

                    statinfo = os.stat(video_name)
                    statinfo = statinfo.st_size

                    if statinfo > 50000:
                        counter += 1

                length_folder = len(liste)

            return JsonResponse({"verification" : counter, "number":length_folder})



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


def treat_video(request):

    if request.method == 'POST':

        #We recuperate a post request = video.
        video_name = request.POST.get('video_name')
     
        print("Treatment video of : ", video_name)

        if video_name:

            print("\nsearching the video into media folder : ", str(video_name))

            name_video = media_path.format(str(video_name))
            print(name_video)

            #Treat file (cut video all 20 seconds).
            video_capture_treament(name_video, dlib_model)

            return JsonResponse({"end_video_treatment" : "video_name"})



@csrf_protect
def home(request):
    """Home template, principal template. Is made up of an access to the site and
    sections to present the project (eyes, face, head, hand, langage sections)."""

    form = video_upload_form(request.POST, request.FILES)
    return render(request, "Home.html", {'form':form})




