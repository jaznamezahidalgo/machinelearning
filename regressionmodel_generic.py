# -*- coding: utf-8 -*-
"""RegressionModel_Generic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ccjSkQNhcWTCmniBAaKMGyHS3IF8cm03
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

import numpy as np

class RegressionModel(object):
  def __init__(self, name):
    self.model = LinearRegression()
    self.name = name

  def __getattr__(self, name: str):
      return object.__getattribute__(name)

  def __setattr__(self, name: str, value):
      self.__dict__[name] = value  

  def split_data(self, X : array, y : array, with_scaled : bool = False, test_size : float = 0.2):
    """ Divide la data para entrenamiento y prueba

    X : valores X (variables independientes)
    y : valores y (variable dependiente)
    with_scaled : indicador para escalado de la data, en caso de que sea True se usa StandardScaler
    test_size : proporción de la data que será considerada para pruebas

    returns None
    """
    self.scaled_data(X)
    X_selected = self.X_features_scaled if with_scaled else X
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_selected, y, 
                                                    test_size = test_size, random_state=29)    
  def train(self):
    """ Entrena el modelo

    returns None
    """
    self.model.fit(self.X_train, self.y_train)

  def make_predictions(self):
    """ Realiza predicciones con el modelo, usando la data de prueba

    returns None
    """
    self.predictions = self.model.predict(self.X_test)

  def make_one_prediction(self, X : np.array):
    """ Realiza una predicción con la data incluida en X

    X : data que será usada en la predicción

    returns np.array con las predicciones para los valores de X
    """
    return self.model.predict(X)

  def metrics(self):
    """ Imprime y retorna las métricas del modelo de regresión

    returns score en entrenamiento, score en prueba, r2 score y MSE

    """
    train_score = self.model.score(self.X_train, self.y_train)
    test_score = self.model.score(self.X_test, self.y_test)
    r2 = r2_score(self.y_test, self.predictions)
    mse = mean_squared_error(self.y_test, self.predictions)
    print("* Metrics of {} *".format(self.name))
    print("-"*40)
    print("\tTrain score :{}".format(train_score))
    print("\tTest score : {}".format(test_score))    
    print("\tModel score : {}".format(r2))    
    print("\tMSE model : {}".format(mse))
    return train_score, test_score, r2, mse
  
  def view_equation(self, x_label : str, y_label : str):
  """ Muestra la gráfica de la ecuación de regresión (genera excepción en caso de que el nombre de la columna no exista)

  x_label : nombre de la etiqueta del eje X
  y_label : nombre de la etiqueta del eje Y

  returns None

  """
    try:
      plt.scatter(self.X_train, self.y_train, color = 'blue')
      plt.plot(self.X_train, self.model.predict(self.X_train), color = 'black')
      plt.title("{0} versus {1}".format(y_label, x_label), fontsize=18)
      plt.xlabel(x_label, fontsize=14, fontweight="bold")
      plt.ylabel(y_label, fontsize=14)
      plt.show()    
    except:
      raise ValueError('Imposible generar gráfico. Verifique se trate de regresión lineal simple')

  def scaled_data(self, X : np.array):
    """ Estandariza los datos usando StandardScaler

    X : datos a estandarizar

    returns None
    """
    scaler = StandardScaler()
    self.X_features_scaled = scaler.fit_transform(X)    

  def __str__(self):
    return "Coeficients : {0}\nIntercept : {1}".format(self.model.coef_, self.model.intercept_)