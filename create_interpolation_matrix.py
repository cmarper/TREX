import numpy as np
import matplotlib as plt
from scipy import interpolate
from matplotlib . mlab import griddata

#x et y sont les coordonnees des pics et z les valeurs de correction
x = [175, 338, 505, 253, 419, 165, 334, 499, 248, 414, 163, 332, 497]
y = [121, 121, 121, 201, 201, 283, 283, 283, 370, 370, 453, 453, 453]
z = [33.69473684, 18.59393939, 37.72, 14.68108108, 15.20571429, 12.77333333, 15.99487179, 13.48421053, 15.33, 7.155, 14.11764706, 9.230769231, 7.255555556]

#on interpole les valeurs de z sans le plan (xy) de maniere lineaire
grid_x = np.linspace(0,640,640)
grid_y = np.linspace(0,480,480)
grid_z = griddata(x, y, z, grid_x, grid_y, interp=’linear ’)

#definition de la matrice de correction
mat = np.array(grid_z)

#on transforme les points non definis par des coefficients 1
mat = np.where(np.isnan(mat), 1, mat)

#ecriture d’un fichier text pour stocker la matrice
np.savetxt(’matrice_correction.txt’, mat)