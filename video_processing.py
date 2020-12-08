# Mon script OpenCV : Video_processing


#Importation des librairies
import numpy as np
import cv2

#Recupere la frame et la retourne
def frame_processing(imgc):
     return imgc


if __name__ == '__main__':

    #Creation d'un objet VideoCapture pour capturer une vidéo
    cap = cv2.VideoCapture('Images2020/jurassicworld.mp4')

    #Boucle à l'infini
    while (True):

        #Capture chaque frame et retourne (Vrai/Faux) si la frame est lu correctement
        ret, frame = cap.read()
        print(ret,frame)

        #Si la frame est lue correctement
        if ret == True:

            #Duplique la frame capturé
            img = frame.copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #Recupere la frame retourné par frame_processing
            gray = frame_processing(gray)

            #Affichage des frames
            cv2.imshow('MavideoAvant', frame)
            cv2.imshow('MavideoApres', gray)

        else:
            print('video ended')
            break

        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()