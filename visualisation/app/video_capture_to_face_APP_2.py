import time

start_time_import = time.time()

import cv2
import numpy as np

from .recuperate_points.face_points import recuperate_landmarks
from .recuperate_points.face_points import head_points
from .recuperate_points.face_points import get_face_in_box
from .recuperate_points.face_points import eyes_points_for_head_analysis


#Pupil part
from .pupille_tracker.pupille_tracker import pupille_tracker

#Path to model, to media folder.
from .paths import media_path, dlib_model
from .paths import path_eyes_detector_stuff
from .paths import data_save
from .paths import path_data_video
from .paths import video_save_media

#Blink part
from .blinking.blinking_eyes import blinking_eyes
from .blinking.blinking_eyes import blink_analysis

#Load dlib model
from .recuperate_points.face_points import load_model_dlib


print("Import time : ", time.time() - start_time_import)



def put_picture(eyes, image_appli):

    #Image resize by contribution of mask region.
    image = cv2.resize(image_appli, (eyes[2].shape[1], eyes[2].shape[0]))

    #If background is blue del it.
    #else replace it by the picture animation.
    for i in range(eyes[2].shape[0]):
        for j in range(eyes[2].shape[1]):

            if image[i, j][0] > 200 and\
               image[i, j][1] > 200 and\
               image[i, j][2] < 60:
                pass
            else:
                eyes[2][i, j] = image[i, j]



def video_capture_to_face(video_path, video_name, eyes_image, blink_image):

    print("Recuperate dimensions of video.")

    #Initialise video.
    cap = cv2.VideoCapture(video_path)

    #Recuperate video informations.
    frame_width  = int(cap.get(3))  #width.
    frame_height = int(cap.get(4))  #height.
    frame_sec = cap.get(cv2.CAP_PROP_FPS)   #Frame per second.

    print("Dimensions recuperate.\n")

    print("Empty file created.")
    print("path : ", video_save_media)

    #Empty video file.
    video_path = video_save_media.format(video_name + ".mp4")
    video_path1 = video_save_media.format(video_name + "1.mp4")
    print("path video : ", video_path)

    writting_animation = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'X264'), int(frame_sec),
                          (int(frame_width), int(frame_height)))

    writting_pupil = cv2.VideoWriter(video_path1, cv2.VideoWriter_fourcc(*'X264'), int(frame_sec),
                          (int(frame_width), int(frame_height)))
 
    #Load DLIB.
    predictor, detector = load_model_dlib(dlib_model)

    #Download picture animation.
    eyes_image = cv2.imread(eyes_image)
    blink_image = cv2.imread(blink_image)
    print("\nPicture animations found.")
    print("\nTreatment in course...")

    oContinuer = True
    while oContinuer:

        start_time_frame = time.time()

        ret, frame = cap.read()
        _, frame_animation = cap.read()
        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #Recuperate landmarks and head box.
            landmarks, head_box = head_points(gray, predictor, detector) #face_points.

            if landmarks is not None:

                #Recuperate pupil center, eyes constitution = (x, y), crop.
                right_eye, left_eye = pupille_tracker(landmarks, frame, gray, head_box, "", "yes")
                #cv2.imshow("frame_dlib", frame)

                right_eye, left_eye = pupille_tracker(landmarks, frame_animation, gray, head_box, "", "no")

                #Savegarde video.
                writting_pupil.write(frame)


                #Recuperate blink algorythme.
                _, result = blinking_eyes(landmarks, head_box) #blinking_eyes.

                if result == "BLINK":   #Blink animation.
                    if right_eye[0] is not None:
                        put_picture(right_eye, blink_image) #replace region by animation.

                    if left_eye[0] is not None:
                        put_picture(left_eye, blink_image)

                elif result != "BLINK": #Eyes animations

                    if right_eye[0] is not None:
                        put_picture(right_eye, eyes_image)

                    if left_eye[0] is not None:
                        put_picture(left_eye, eyes_image)


            #Savegarde video.
            writting_animation.write(frame_animation)

            #Animations.
            #cv2.imshow("c", frame_animation)
            
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break


        else:
            oContinuer = False
            return "/media/video_save/" + str(video_name) + ".mp4", "/media/video_save/" + str(video_name) + "1.mp4"


    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":

    blink_image = r"C:\Users\jeanbaptiste\Desktop\SYNERGO_SITE\Synergo\media\eyes_detector\fermture_gros_oeil.png"
    eyes_image = r"C:\Users\jeanbaptiste\Desktop\SYNERGO_SITE\Synergo\media\eyes_detector\gros_oeil.png"
    video_capture_to_face("g.mp4", "", eyes_image, blink_image)






