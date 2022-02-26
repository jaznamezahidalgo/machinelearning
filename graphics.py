# graphics.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def barplot(values : pd.DataFrame, title :str, labels : np.array):
  """
  values : Dataframe que contiene la columna que se quiere graficar y sus frecuencias
  """
  # Tamaño del gráfico: (ancho, largo)
  plt.figure(figsize=(8,8))

  # Usamos el gráfico de barras de seaborn
  sns.barplot(x=values.index, y=values.values.flatten(), edgecolor='black')

  # Asignamos etiquetas a eje x, y asi como tambien el titulo del gráfico
  plt.xlabel(labels[0], fontsize=14)
  plt.ylabel(labels[1], fontsize=14)
  plt.title(title, fontsize=18, fontweight="bold")

  plt.show() 

def piechart(values : pd.DataFrame, title : str, exp : np.array):
  frecuencias = values.values.flatten()
  # Etiqueta de cada trozo
  etiquetas = values.index

  plt.figure(figsize=(10,10))

  plt.title(title, fontsize=18, fontweight="bold")
  plt.pie(frecuencias, labels = etiquetas, explode = exp, autopct='%2.1f%%')
  plt.show()  