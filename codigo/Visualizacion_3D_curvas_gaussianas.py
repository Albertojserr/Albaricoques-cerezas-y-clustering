
#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro:
# @Capítulo: 9 - Albaricoques, cerezas y clustering
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   SCIKIT-LEARN : 0.21.0
#   MATPLOTLIB : 3.0.3
#   JOBLIB : 0.13.2
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#   #-----------------------------------------------------------------------------------------

import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import os
from mpl_toolkits.mplot3d import axes3d, Axes3D



dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

class Visualizacion3D:

    def __init__(self):

        self.frutas = pnd.read_csv(dir_path+"/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)

        self.n_components = 2

    # Extraer x e y
    def extraccion(self):

        self.x = self.frutas.DIAMETRO
        self.y = self.frutas.PESO

    # Define los límites
    def limites(self):
        self.deltaX = (max(self.x) - min(self.x))/10
        self.deltaY = (max(self.y) - min(self.y))/10
        self.xmin = min(self.x) - self.deltaX
        self.xmax = max(self.x) + self.deltaX
        self.ymin = min(self.y) - self.deltaY
        self.ymax = max(self.y) + self.deltaY
        print(self.xmin, self.xmax, self.ymin, self.ymax)

    # Crear meshgrid
    def meshgrid(self):
        self.xx, self.yy = np.mgrid[self.xmin:self.xmax:100j, self.ymin:self.ymax:100j]

        posiciones = np.vstack([self.xx.ravel(), self.yy.ravel()])
        values = np.vstack([self.x, self.y])
        kernel = st.gaussian_kde(values)
        f = np.reshape(kernel(posiciones).T, self.xx.shape)

        fig = plt.figure(figsize=(8,8))
        ax = fig.gca()
        ax.set_xlim(self.xmin, self.xmax)
        ax.set_ylim(self.ymin, self.ymax)
        cfset = ax.contourf(self.xx, self.yy, f, cmap='coolwarm')
        ax.imshow(np.rot90(f), cmap='coolwarm', extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        cset = ax.contour(self.xx, self.yy, f, colors='k')
        ax.clabel(cset, inline=1, fontsize=10)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.show()

        fig = plt.figure(figsize=(13, 7))
        ax = plt.axes(projection='3d')
        surf = ax.plot_surface(self.xx, self.yy, f, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        fig.colorbar(surf, shrink=0.5, aspect=5) # añadir barra de color indicando el PDF
        ax.view_init(60, 35)
        plt.show()

    @staticmethod
    def ejecutar():
        vis=Visualizacion3D()
        vis.extraccion()
        vis.limites()
        vis.meshgrid()

if __name__=='__main__':
    vis=Visualizacion3D()
    vis.ejecutar()
