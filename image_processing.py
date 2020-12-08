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
    img = cv2.imread('Images2020/boats.jpg')

    #Converti l'image de l'espace couleur BGR en espace couleur Gris
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applicage de l'operateur laplacien à l'image img
    # Calcul dérivé de l'image img en fonction des changements horizontaux (Operateur Sobel)
    # Calcul dérivé de l'image img en fonction des changements verticaux (Operateur Sobel)
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    #Ajout des images à la figure
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    #Affichage de la figure
    plt.show()