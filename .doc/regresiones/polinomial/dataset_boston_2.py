#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Regresión Lineal Simple

dataset: boston = Versión Ampliada

"""

from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   
import statistics

boston = load_boston()
X = boston.data
y = boston.target

x = range(0, boston.data.shape[0],1)  # Igual que x = range(0, len(y),1)

CRIME = 0; ZN = 1; INDUSTRIAL = 2; ROOMS = 5; DISTANCE = 7; 

# Se grafican varias características
plt.figure(figsize=(30,8))
plt.plot(x, X[:,INDUSTRIAL], 'y-', label = 'Industrial')
plt.plot(x, X[:,DISTANCE], 'b-', label = 'Distancia')
plt.plot(x, X[:,ROOMS], 'c-', label = 'Habitaciones')
plt.rcParams.update({'font.size':18});
plt.legend(prop={'size':22}); plt.grid(); 


# In[9]:



# print (boston.DESCR) Información textual del dataset

# Este dataset contiene 506 muestras (filas) y 13 características (columnas)
print(X.shape) 

# Este dataset es adecuado para regresion. El objetivo son números
print(y.shape)

print(X[0:3,:]) # imprime filas de datos, empezando en la fila 0 hasta la fila 3-1
print(y[0:5]) # fila de objetivos, empezando desde la fila 0 hasta la fila 5-1
print(X[1,ZN]) # imprime la característica ZN desde la tercera fila
print(X[1:3,CRIME]) # imprime la característica CRIME para las filas 1 y 2
print(boston.data.shape[0])
print(boston.data.shape[1])

# Obtiene la media y la varianza de cada característica
mean = []; variance = []
for i in range(boston.data.shape[1]):
    mean.append(statistics.mean(X[:,i]))
    variance.append(statistics.variance(X[:,i])) 

# Imprime la media y la varianza de cada característica
for i in range(boston.data.shape[1]):
    print(format(i) + " media: {:.2f}".format(mean[i]) + ", varianza: {:.2f}".format(variance[i]))

fig, axs = plt.subplots(1,2, figsize=(7,4))

# Gráfica de dispersión 3D de las dos figuras
axs[1] = Axes3D(fig, elev=40, azim=-30)
axs[1].scatter(X[:,DISTANCE], X[:,ROOMS], y, c='b', marker='o')
axs[1].set_xlabel('Distancia', fontsize=22)
axs[1].set_ylabel('Habitaciones', fontsize=22)
axs[1].set_zlabel('Precio', fontsize=22) 

plt.show()

