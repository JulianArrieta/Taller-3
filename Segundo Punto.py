# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:45:58 2022

@author: USUARIO
"""

#Librerías
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#---------------------------------------------------------------------
#Para empezar, al correr el programa, se tendrá que establecer el tamaño de ambas muestras
n = int(input("tamaño: "))
#Experimento A
#Aquí se definen la media y la desviación estandar del Experimento A
print("Experimento A")
mu_a = int(input("Media: "))
std_a = int(input("Desviación estandar: "))
a = np.random.normal(loc = mu_a, scale = std_a , size = n)
exp_a = pd.DataFrame(a)
exp_a.to_csv("Experimento_a.csv", index= False)
Experimento_a = pd.read_csv("Experimento_a.csv" )
#Aquí se exporta e importa automaticamente
#El nombre del DF importado es: Experimento_A

#Experimento B
#Aquí se definen la media y la desviación estandar del Experimento B
print("Experimento B")
mu_b = int(input("Media: "))
std_b = int(input("Desviación estandar: "))
b = np.random.normal(loc = mu_b, scale = std_b , size = n)
exp_b = pd.DataFrame(b)
exp_b.to_csv("Experimento_b.csv", index= False)
Experimento_b = pd.read_csv("Experimento_b.csv" )
print("------------------------------------------------------------------------------")
#Aquí se exporta e importa automaticamente
#El nombre del DF importado es: Experimento_A
#---------------------------------------------------------------------
#MENÚ
#Una vez hecho lo anterior se genera un menú
#En el menú se podrá elegir entre distintas opciones para realizar sobre ambas muestras

i = 0
while i!= 1:
    print("1. indicar si la diferencia en la media de los datos es estadísticamente significativa.")
    print("2. mostrar en pantalla la correlación de Pearson y Spearman de los datos.")
    print("3. graficar el diagrama de dispersión y la línea recta que aproxime los datos calculada por una regresión lineal por mínimos cuadrados.")
    print("4. Salir")
    val = int(input("Escoja una opción: "))
    if val == 1:
        ph = stats.ttest_ind(Experimento_a["0"], Experimento_b["0"])
        pv = round(ph[1],3)
        if pv > 0.05:
            print("-------------------------------------------------------")
            print(f"El p valor, {pv}, es mayor que 0.05 por lo que la diferencia entre medias no es estadisticamente significativa" )
            print("-------------------------------------------------------")
        elif pv <= 0.05:
            print("-------------------------------------------------------")
            print(f"El p valor, {pv}, es menor o igual que 0.05 por lo que la diferencia entre medias es estadisticamente significativa" )    
            print("-------------------------------------------------------")    
    #--------------------------------------------------------------------
    elif val == 2:
        print("-------------------------------------------------------")
        print("Correlación pearson: ", Experimento_a["0"].corr(Experimento_b["0"], method = 'pearson'))
        print("Correlación spearman: ", Experimento_a["0"].corr(Experimento_b["0"], method = 'spearman'))
        print("-------------------------------------------------------")
    #--------------------------------------------------------------------
    elif val == 3:
        datos = {'a' : Experimento_a["0"], 'b' : Experimento_b["0"]}
        exps = pd.DataFrame(datos)  
        sb.lmplot(x = 'a', y = 'b', data = exps)
    elif val == 4:
        i = 1
    else:
        print("No hago nada")
        




