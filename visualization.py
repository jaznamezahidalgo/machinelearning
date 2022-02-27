import matplotlib.pyplot as plt
import numpy as np

class Visualization(object):
  def __init__(self, data_frame):
    self.data_frame = data_frame

  def __getattr__(self, name: str):
    return object.__getattribute__(name)

  def __setattr__(self, name: str, value):
    self.__dict__[name] = value 

  def histogram(self, column :str, num_bins : int, title: str, labels : np.array):
    # Tamaño del grafico: (ancho, largo)
    plt.figure(figsize=(8,8))
    # Definimos a Matplotlib que es un histograma con los valores de y agrupados en num_bis
    plt.hist(self.data_frame[column], num_bins, edgecolor='black')

    # Asignamos Nombres a eje x, y asi como tambien el titulo del grafico
    plt.xlabel(labels[0], fontsize=14)
    plt.ylabel(labels[1], fontsize=14)
    plt.title(title, fontsize=18, fontweight="bold")

    plt.show()        

  def piechart_by_interval(self, title :str, column : str, exp : np.array):
    # Obtiene los valores
    values = self.data_frame[column]
    # Obtiene los límites
    lim_inf = min(values)
    lim_sup = max(values)
    q1 = np.percentile(values, 25)
    q2 = np.percentile(values, 50)
    q3 = np.percentile(values, 75)     

    # Obtiene las frecuencias de cada intervalo
    frecuencias = np.zeros(4)
    frecuencias[0] = values.loc[values < q1].count()
    frecuencias[1] = values.loc[(values >= q1) & (values < q2)].count()
    frecuencias[2] = values.loc[(values >= q2) & (values < q3)].count()
    frecuencias[3] = values.loc[values >= q3].count()   

    # Etiqueta de cada trozo
    m = ['Menos de {}'.format(q1),'Entre {0} y {1}'.format(q1, q2),
        'Entre {0} y {1}'.format(q2, q3), '{} o más'.format(q3)]

    plt.figure(figsize=(10,10))

    plt.title(title, fontsize=18, fontweight="bold")
    plt.pie(frecuencias, labels = m, explode = exp, autopct='%2.1f%%')
    plt.show()     

  def piechart(self, column : str, title : str, labels : np.array):
    plt.figure(figsize=(8,8))
    plt.pie(self.data_frame[column].value_counts(), labels = labels, autopct='%2.1f%%')
    plt.title(title, fontsize=18, fontweight="bold")
    plt.show()     