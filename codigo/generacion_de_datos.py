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



#---- IMPORTAR MÓDULOS --
import random
import pandas as pnd
import os

#---- CARACTERÍSTICAS------

class Generación:

    def __init__(self, caracteristicasCerezas=None, caracteristicasAlbaricoques=None):
        #CEREZAS
        self.caracteristicasCerezas = caracteristicasCerezas

        #ALBARICOQUES: ATENCIÓN DOS CASOS DE PRUEBAS EN FUNCIÓN DEL AVANCE DE SU LECTURA
        self.caracteristicasAlbaricoques = caracteristicasAlbaricoques

    #GENERACION DE LOS DATOS
    def generacionDatos(self):
        # [DIAMETRO, PESO]
        self.cantidadObservaciones = 200

    def generacionCerezas(self):
        #Generación de las cerezas
        self.cerezas = []
        random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            self.cereza = random.choice(self.caracteristicasCerezas)
            #Generación de un diámetro
            diametro = round(random.uniform(self.cereza[0], self.cereza[1]),2)
            #Generación de un peso
            peso = round(random.uniform(self.cereza[2], self.cereza[3]),2)
            print ("Cereza "+str(iteration)+" "+str(self.cereza)+" : "+str(diametro)+" - "+str(peso))
            self.cerezas.append([diametro,peso])

    def generacionAlbaricoques(self):
    #Generación de los albaricoques
        self.albaricoques = []
        random.seed()
        for iteration in range(self.cantidadObservaciones):
            #elección al azar de una característica
            self.albaricoque = random.choice(self.caracteristicasAlbaricoques)
            #Generación de un diámetro
            diametro = round(random.uniform(self.albaricoque[0], self.albaricoque[1]),2)
            #Generación de un peso
            limiteMinPeso = self.albaricoque[2] / 1.10
            limiteMaxPeso = self.albaricoque[2] * 1.10
            peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
            print ("Albaricoque "+str(iteration)+" "+str(self.albaricoque)+" : "+str(diametro)+" - "+str(peso))
            self.albaricoques.append([diametro,peso])

    #Constitución de las observaciones
    def constitucion(self):
        self.frutas = self.cerezas+self.albaricoques
        print(self.frutas)

    #Mezcla de las observaciones
    def mezcla(self):
        random.shuffle(self.frutas)

    #Guardado de las observaciones en un archivo
    def guardar(self):
        dataFrame = pnd.DataFrame(self.frutas)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        dataFrame.to_csv(dir_path+"/datas/frutas.csv", index=False,header=False)

    @staticmethod
    def ejecutar():
        caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
        caracteristicasAlbaricoques =[[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
        gen= Generación(caracteristicasCerezas, caracteristicasAlbaricoques)
        gen.generacionDatos()
        gen.generacionCerezas()
        gen.generacionAlbaricoques()
        gen.constitucion()
        gen.mezcla()
        gen.guardar()

if __name__=='__main__':
    Generación().ejecutar()




