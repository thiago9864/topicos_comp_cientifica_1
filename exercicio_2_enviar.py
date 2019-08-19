# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:33:38 2019

@author: Thiago
"""

import matplotlib.pyplot as plt
import numpy as np

#intervalo de tempo
t0 = 0.0 
tf = 1000.0

#condição inicial
s0=10.0
e0=2.0
c0=0.0
p0=0.0

#parametros
k1 = 0.01 #k+1
k2 = 0.02 #k-1
k3 = 0.03 #k+2

n = 1000
dt = (tf - t0) / (n-1)
t = np.linspace(t0, tf, n)

#arrays de solução
S = np.zeros([n])
E = np.zeros([n])
C = np.zeros([n])
P = np.zeros([n])

#aplica condição inicial
S[0] = s0
E[0] = e0
C[0] = c0
P[0] = p0

#calcula metodo
for i in range(1,n):
    S[i] = dt * (k2 * C[i-1] - k1*S[i-1]*E[i-1]) + S[i-1]
    E[i] = dt * ((k2+k3) * C[i-1] - k1*S[i-1]*E[i-1]) + E[i-1]
    C[i] = dt * (-1*(k2+k3) * C[i-1] + k1*S[i-1]*E[i-1]) + C[i-1]
    P[i] = dt * (k3 * C[i-1]) + P[i-1]
    
#Visualizando as soluções
plt.plot(t, S, 'r', label=u'S')
plt.plot(t, E, 'b', label=u'E')
plt.plot(t, C, 'g', label=u'C')
plt.plot(t, P, 'y', label=u'P')

plt.legend(loc='upper right')

plt.show()