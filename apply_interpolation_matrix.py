import imageio
import numpy
from matplotlib . pyplot import ∗

#on lit l’image et on la convertit en array
img = imageio.imread("ligne.tif")

#Visualisation de l'image : #tabimg=img[: ,: ,0]
#imshow ( img )
#colorbar ()

#Application de la matrice de correction
imgcorrige = np.multiply(mat,img)

#affichage en couleur
imshow(imgcorrige , cmap='gray')
colorbar ()

#enregistrement de l’image en .png
imageio.imwrite('ligne_corrigee.png',imgcorrige)
