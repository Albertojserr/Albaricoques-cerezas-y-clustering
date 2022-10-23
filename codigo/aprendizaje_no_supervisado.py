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
#-----------------------------------------------------------------------------------------


import pandas as pnd
import matplotlib.pyplot as plt
import os

from sklearn.cluster import KMeans

from sklearn import mixture

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
#para cogerlo de otra carpeta usamos lo siguiente
#dir_path=dir_path+"/../teoria"
#Carga de datos
class Aprendizaje:
    def __init__(self):
        self.frutas = pnd.read_csv(dir_path+"/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)
    def vis(self):
#Visualización gráfica de los datos
        self.frutas.plot.scatter(x="DIAMETRO",y="PESO")
        plt.title("Frutas del dataset")
        plt.show()


        #Aprendizaje con el algoritmo K-Mean

    def aprKMeans(self):
        self.modelo=KMeans(n_clusters=2)
        self.modelo.fit(self.frutas)

        #Predicciones
        predicciones_kmeans = self.modelo.predict(self.frutas)

        #Visualización de la clusterización
        plt.scatter(self.frutas.DIAMETRO, self.frutas.PESO, c=predicciones_kmeans, s=50, cmap='viridis')
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")

        #Visualización de los centroides
        centers = self.modelo.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
        plt.title("Centroides")
        plt.show()

#Guardar el modelo (eliminar marca de comentario # si es necesario)
#from joblib import dump
#dump(modelo,'modelos/kmean.joblib')

#--- Realización de las clasificaciones --
#CEREZA: 26,98 mm de diametro ,8,75 gramos
#ALBARICOQUE: 55,7  mm de diámetro , 102,16 gramos

    def clasificaciones(self):
        cereza = [[26.98,8.75]]
        numClusterC = self.modelo.predict(cereza)
        print("Número de clúster de las cerezas: "+ str(numClusterC))


        albaricoque = [[55.7,102.16]]
        numClusterA = self.modelo.predict(albaricoque)
        print("Número de clúster de los albaricoques: " + str(numClusterA))

#Instrucciones a adaptar en función de los números de clústeres
#determinados con anterioridad:
    #Para saber cual de los dos cluster es el de cerezas y cual el de albaricoques
    def busqueda(self):
        cereza = [[26.98,8.75]]
        numCluster = self.modelo.predict(cereza)
        if int(numCluster)==0:
            print("¡Es un albaricoque!")
        else:
            print("¡Es una cereza! ")


        albaricoque = [[55.7,102.16]]
        numCluster = self.modelo.predict(albaricoque)
        if int(numCluster)==0:
            print("¡Es un albaricoque!")
        else:
            print("¡Es una cereza!")


#---- Modelo de mezclas Gaussianas (GMM) -----------

    def Gauss(self):
#Determinación de los clústeres (encontrar 2)
        gmm = mixture.GaussianMixture(n_components=2)

        #Aprendizaje
        gmm.fit(self.frutas)

        #Clasificación
        clusteres = gmm.predict(self.frutas)

        #Visualización de los clústeres
        plt.scatter(self.frutas.DIAMETRO, self.frutas.PESO, c=clusteres, s=40, cmap='viridis');
        plt.xlabel("DIAMETRO")
        plt.ylabel("PESO")
        plt.title("Mezcla Gaussiana")
        plt.show()
    @staticmethod
    def ejecutarKMeans():
        apr=Aprendizaje()
        #primer plot con los datos de las frutas
        apr.vis()
        #segundo plot, con los centroides
        apr.aprKMeans()
        apr.clasificaciones()
        apr.busqueda()
    @staticmethod
    def ejecutarGauss():
        apr=Aprendizaje()
        apr.Gauss()
    @staticmethod
    def ejecutar():
        aprendizaje=Aprendizaje()
        eleccion=input("Elige: [KMeans,Gauss]")
        if eleccion.lower()=="kmeans":
            aprendizaje.ejecutarKMeans()
        else:
            aprendizaje.ejecutarGauss()