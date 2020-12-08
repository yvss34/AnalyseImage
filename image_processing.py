# Image Processing with OpenCV

#Importation des librairies
import cv2
import os
import sys
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':


    #Affichage de la version de Python et de ses composants et d'OpenCV
    print("Python version")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)
    print("OPENCV Version =", cv2.__version__)

    #Affichage du répertoire de travail actuel du processus
    rep_cour = os.getcwd()
    print(rep_cour)

    #Lecture/Chargement d'une l'image
    img = cv2.imread('Images2020/lisa.png')

    #Converti l'image de l'espace couleur BGR en espace couleur Gris
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Filtre moyenneur
    filtre5 = cv2.blur(img,(2,2))

    #Ajout des images à la figure
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(filtre5,cmap = 'gray')
    plt.title(''), plt.xticks([]), plt.yticks([])


    #Affichage de la figure
    plt.show()