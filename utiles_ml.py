# -*- coding: utf-8 -*-
"""utiles_ml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uiyuY0j4v7KBM4QiJ_-Kl0VcD8_WFgQW
"""

from sklearn.metrics import mean_squared_error, r2_score
def selected_features(data_frame, lst_features):
  return data_frame[lst_features]

def metrics_regression(model, X_train, y_train, X_test, y_test, y_pred):
  print("Train score {}".format(model.score(X_train, y_train)))
  print("Test score {}".format(model.score(X_test, y_test)))    
  print("Model score {}".format(r2_score(y_test, y_pred)))    
  print("MSE model {}".format(mean_squared_error(y_test, y_pred)))
  return model.score(X_train, y_train), model.score(X_test, y_test), r2_score(y_test, y_pred), mean_squared_error(y_test, y_pred)