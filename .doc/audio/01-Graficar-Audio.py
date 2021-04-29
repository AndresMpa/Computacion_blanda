#!/usr/bin/env python
# coding: utf-8

# In[4]:


# GRAFICAR ARCHIVO DE AUDIO

# Importar las librerías 
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile


# In[5]:



# Lee el archivo de audio
frecuencia_muestreo, senial = wavfile.read('sonido_aleatorio.wav')

# Mostrar los parámetros
print('\nTamaño señal:', senial.shape)
print('Tipo de dato:', senial.dtype)
print('Duracción de la señal:', round(senial.shape[0] / float(frecuencia_muestreo), 2), 'seconds')
print('Frecuencia de muestreo: ', frecuencia_muestreo)


# In[6]:


# Normalizar la señal
senial = senial / np.power(2, 15)

# Extraer los primeros 50 valores
senial = senial[:50]

# Construir el eje de tiempo en milisegundos
eje_del_tiempo = 1000 * np.arange(0, len(senial), 1) / float(frecuencia_muestreo)

# Dibujar la señal de audio
plt.plot(eje_del_tiempo, senial, color='black')
plt.xlabel('Tiempo (milisegundos)')
plt.ylabel('Amplitud')
plt.title('Señal Entrada de Audio')
plt.show()

