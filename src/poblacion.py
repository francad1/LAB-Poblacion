# -*- coding: utf-8 -*-

""" 
Poblacion mundial
@author: Toñi Reina
REVISOR: José Antonio Troyano, Daniel Mateos, Mariano González, Fermín Cruz
ÚLTIMA MODIFICACIÓN: 10/10/2022
"""

import csv
from matplotlib import pyplot as plt
from collections import namedtuple

RegistroPoblacion = namedtuple("RegistroPoblacion", "pais, codigo, año, censo")

############################################################################################
def lee_poblaciones(ruta_fichero):
    
    with ruta_fichero as archivo:

        reader=csv.reader(archivo)
        registros=[]
        for line in reader:
            pais=str(line[0])
            codigo = str(line[1])
            año = int(line[2])
            censo= int(line[3])
            registro= RegistroPoblacion(pais,codigo,año,censo)
            registros.append(registro)

        return registros


def calcula_paises(poblaciones):
    """
    Calcula la lista de países distintos presentes en una lista de de tuplas de tipo RegistroPoblacion.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)

    @return: lista de paises, ordenada alfabéticamente, sin duplicados
    @rtype: list(str)

    """
    paises=[]
    for e in poblaciones:
        paises.append(e[0])
    pais_sin_duplicados= list(set(paises))
    pais_sin_duplicados.sort()

    return pais_sin_duplicados


def filtra_por_pais(poblaciones, pais_o_codigo):
    """
    Devuelve el año y el censo de las tuplas correspondientes a un determinado pais

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se seleccionarán los registros
    @type pais_o_codigo: str

    @return: lista de tuplas (año, censo) seleccionadas
    @rtype: list(tuple(int, int))
    """
    filtrado_por_pais=[]
    for e in poblaciones:
        if e[0]==pais_o_codigo or e[1]==pais_o_codigo:
            filtrado_por_pais.append(e)
    return filtrado_por_pais


    pass


##############################################################################################

##############################################################################################
def filtra_por_paises_y_anyo(poblaciones, año, paises):
    """
    Devuelve el país y el censo de las tuplas correspondientes a un conjunto de paises de un año concreto.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: año del que se seleccionarán los registros
    @type año: int
    @param paises: conjunto de nombres de países de los que se seleccionarán los registros
    @type paises: set(str)

    @return: lista de tuplas (pais, censo) seleccionadas
    @rtype: list(tuple(str,int))
    """
    pais_anyo=[]
    for e in poblaciones:
        if e[2]==año:
            for i in list(paises):
                if e[0] == i:
                    tupla=(e[0],e[3])
                    pais_anyo.append(tupla) 
    return pais_anyo


    pass


##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais_o_codigo):
    """
    Genera una curva con la evolución de la población de un país. El país puede
    darse como su nombre completo o por su código.

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param pais_o_codigo: nombre o código del país del que se generará la gráfica
    @type pais_o_codigo: str
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_años y lista_habitantes
    titulo = "Evolución de " + pais_o_codigo
    lista_años = []
    lista_habitantes = []

    for e in poblaciones:
        if e[0] == pais_o_codigo or e[1]==pais_o_codigo:
            lista_años.append(e[2])
            lista_habitantes.append(e[3])

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()


###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, año, paises):
    """
    Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto

    @param poblaciones: lista de tuplas con información de poblaciones
    @type poblaciones: list(RegistroPoblacion)
    @param año: del que se generará la gráfica
    @type año: int
    @param paises: nombres de los países para los que se generará la gráfica
    @type paises: list(str)
    """
    # TODO Complete la función para asignar los valores correctos
    #  a las variables titulo, lista_paises y lista_habitantes
    titulo = "Evolucion" + str(paises)
    lista_paises = []
    lista_habitantes = []

    pais_poblacion= filtra_por_paises_y_anyo(poblaciones, año, paises)

    pais_poblacion.sort(key=lambda pais_censo: pais_censo[0])
    for e in pais_poblacion:
        lista_paises.append(e[0])
        lista_habitantes.append(e[1])

    # Estas instrucciones dibujan la gráfica
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
