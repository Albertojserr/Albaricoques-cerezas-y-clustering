
from codigo.aprendizaje_no_supervisado import Aprendizaje
from codigo.generacion_de_datos import Generación
from codigo.Visualizacion_3D_curvas_gaussianas import Visualizacion3D

if __name__=='__main__':
    #en el fichero de generacion_de_datos (para el init)

    caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]
    #Caso 1: (en el fichero de generacion_de_datos (para el init))
    caracteristicasAlbaricoques1 = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
    #caso 2:
    caracteristicasAlbaricoques2 =[[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]
    eleccion=input("Que características de los albaricoques quieres elegir: [1,2]")
    if eleccion=="1":
        caracteristicasAlbaricoques=caracteristicasAlbaricoques1
    else:
        caracteristicasAlbaricoques=caracteristicasAlbaricoques2


    Generación.ejecutar(caracteristicasCerezas,caracteristicasAlbaricoques)
    Aprendizaje.ejecutar()
    continuar= input("Escriba si quiere una visualización en 3D : [Si, no]")
    if continuar!='no':
        Visualizacion3D.ejecutar()





