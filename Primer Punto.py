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
    #Es necesario hacer las opciones 1 y 2 antes de poder hacer las otras
    val = int(input("Escoja una opción: " ))
    if val == 1:
        #La opción 1 exporta el dataframe gapminder al directorio de python donde se estén guardando los archivos
        gapminder.to_excel('gapminder.xlsx', sheet_name='hoja 1', index = False)
    elif val == 2:
        #la opción 2 importa el archivo previamente guardado
        df_nuevo = pd.read_excel("gapminder.xlsx", sheet_name="hoja 1")
        sz = df_nuevo["country"].size
        prcntg = round(sz*0.1)
        sq = list(np.arange(0,sz))
        indices = random.sample(sq, prcntg)
        df_nuevo.loc[indices, ["lifeEXP","pop", "gdpPercap"]] = np.nan
        #Además esta opción también convierte el 10% de los datos de algunas columnas en datos NAn
        print(df_nuevo)
    elif val == 3:
        #Esta opción genera un diagrama de dispersión entre lifeExp y pop
        fig, ax = plt.subplots()
        ax.scatter(df_nuevo["lifeExp"], df_nuevo["pop"] )
        plt.show()
    elif val == 4:
        #Esta opción genera un diagrama de dispersión entre gdpPercap y pop
        fig, ax = plt.subplots()
        ax.scatter(df_nuevo["gdpPercap"], df_nuevo["pop"] )
        plt.show()
    elif val == 5:
        #Esta opción genera un diagrama de cajas discriminaddo por continentes
        #El diagrama es del gdpPercap desde 1990 hasta 2007
        df = df_nuevo[(df_nuevo['year']>1990) & (df_nuevo['year']<2007)]
        df2 = df[["gdpPercap", "continent"]]
        df_filtered = df2[df2["gdpPercap"].notna()]
        africa = df_filtered[(df_filtered['continent'] == 'Africa')]
        africa = africa["gdpPercap"]
        asia = df_filtered[(df_filtered['continent'] == 'Asia')]
        asia = asia["gdpPercap"]
        americas = df_filtered[(df_filtered['continent'] == 'Americas')]
        americas = americas["gdpPercap"]
        europe = df_filtered[(df_filtered['continent'] == 'Europe')]
        europe = europe["gdpPercap"]
        oceania = df_filtered[(df_filtered['continent'] == 'Oceania')]
        oceania = oceania["gdpPercap"]
        cont = [africa, asia, americas, europe, oceania]
        v1 = [1, 2, 3, 4, 5]
        v2 = ['africa', 'asia', 'americas', 'europe', 'oceania']
        plt.boxplot(cont)
        plt.xticks(v1, v2)
        plt.show()
    elif val == 6:
        i = 1
    else:
        print("No hago nada")
    
        
       
            
   
        