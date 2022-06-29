# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#LIBRERIAS 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gapminder import gapminder
import random

i = 0
while i != 1:
    #MENU
    print("1. Guardar gapminder")
    print("2. Leer el archivo gapminder.xlsx")
    print("3. Diagrama de dispersión lifeExp vs pop")
    print("4. Diagrama de dispersión gdpPercap vs pop.")
    print("5. diagramas de cajas de la variable gdpPercap discriminados por continentes desde 1990 a 2007.")
    print("6. Salir")
    #INGRESAR LA OPCIOÓN A REALIZAR
    val = int(input("Escoja una opción: " ))
    if val == 1:
        gapminder.to_excel('gapminder.xlsx', sheet_name='hoja 1', index = False)
    elif val == 2:
        df_nuevo = pd.read_excel("gapminder.xlsx", sheet_name="hoja 1")
        sz = df_nuevo["country"].size
        prcntg = round(sz*0.1)
        sq = list(np.arange(0,sz))
        indices = random.sample(sq, prcntg)
        df_nuevo.loc[indices, ["lifeEXP","pop", "gdpPercap"]] = np.nan
        print(df_nuevo)
    elif val == 3:
        fig, ax = plt.subplots()
        ax.scatter(df_nuevo["lifeExp"], df_nuevo["pop"] )
        plt.show()
    elif val == 4:
        fig, ax = plt.subplots()
        ax.scatter(df_nuevo["gdpPercap"], df_nuevo["pop"] )
        plt.show()
    elif val == 5:
        df = df_nuevo[(df_nuevo['year']>1990) & (df_nuevo['year']<2007)]
        df2 = df["gdpPercap"]
        df_filtered = df2[np.logical_not(np.isnan(df2))]
        fig, ax = plt.subplots()
        ax.boxplot(df_filtered)
        plt.show()
    elif val == 6:
        i = 1
    else:
        print("No hago nada")
    
        
       
            
   
        