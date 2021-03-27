#!/usr/bin/env python
# coding: utf-8

# In[22]:


"""
Regresión Lineal Simple

dataset: boston

"""

# LIBRERÍAS A UTILIZAR

# Se importan la librerias
import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

# PREPARAR LA DATA

# Importamos los datos de la misma librería de scikit-learn
boston = datasets.load_boston()

# Aquí se imprime la DATA recibida
# La información es muy densa. 
# Lo mejor es revisarla por partes, como se verá posteriormente

# A pesar de lo expresado, vamos a imprimir la DATA
print(boston)
print()


# In[23]:


# ENTENDIENDO LA DATA

# Se verifica la información contenida en el dataset
print('Información en el dataset:')
print(boston.keys())
print()

# data: Es el conjunto de los datos almacenados
# target: Son las columnas con el objetivo o respuesta
# feature_names: Nombres de las columnas
# DESCR: Es una descripción completa del contenido del dataset
# filename: Nombre del archivo


# In[24]:


# Se verifican las características del dataset
print('Características del dataset:')
print(boston.DESCR)


# In[25]:


# Se verifica la cantidad de datos que hay en los dataset
print('Cantidad de datos:')
print(boston.data.shape)
print()


# In[26]:


# Se verifica los nombres de las columnas
print('Nombres columnas:')
print(boston.feature_names)


# In[27]:


# PREPARAR LA DATA REGRESIÓN LINEAL SIMPLE

# Seleccionamos solamente la columna 5 del dataset
# (Número de habitaciones)
# Vamos a encontrar la relación entre estas dos variables
X = boston.data[:, np.newaxis, 5]

# Se definen los datos correspondientes a las etiquetas
y = boston.target

# Se grafican los datos correspondientes
plt.scatter(X, y)
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()


# In[28]:


# IMPLEMENTACIÓN DE LA REGRESIÓN LINEAL SIMPLE

from sklearn.model_selection import train_test_split

# Separa los datos de "train" en entrenamiento y prueba 
# para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Se define el algoritmo a utilizar
lr = linear_model.LinearRegression()

# Se entrena el modelo
lr.fit(X_train, y_train)

# Se realizo una predicción
Y_pred = lr.predict(X_test)

# Se grafican los datos junto con el modelo
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title('Regresión Lineal Simple')
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()


# In[29]:


print()
print('DATOS DEL MODELO REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a":')
print(lr.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr.intercept_)
print()
print('La ecuación del modelo es igual a:')
print('y = ', lr.coef_, 'x ', lr.intercept_)

print()
print('Precisión del modelo:')
print(lr.score(X_train, y_train))

