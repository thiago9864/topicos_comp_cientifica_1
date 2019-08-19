# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:19:45 2019

@author: Thiago
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la

t = np.arange(0.0, 5.0, 0.01)
k = 0.5
v0 = 1

plt.plot(t, v0*np.exp(k*t), 'r', label=u'Solução')

plt.legend(loc='upper left')
plt.show()

#%%

t = np.arange(0.0, 5.0, 0.01)
k = 0.5

for v0 in range(0,20,2):
    plt.plot(t, v0*np.exp(k*t), label=u'Solução '+str(v0))

plt.legend(loc='upper left')
plt.show()

#%%

t0 = 0.0 #t inicial
tf = 5.0 #t final
a0 = 1
k = 0.5
n = 100

dt = (tf - t0) / (n-1)
t = np.linspace(t0, tf, n)
a = np.zeros([n])

#aplica condição inicial
a[0] = a0

#calcula metodo
for i in range(1,n):
    a[i] = dt*(k*a[i-1])+a[i-1]
  
#facilitador de leitura
solEuler = a
solAnalitica = a0*np.exp(k*t)


#plota graficos
plt.plot(t, a, 'r', label=u'Euler')
plt.plot(t, a0*np.exp(k*t), 'b', label=u'Solução Exata')

plt.legend(loc='upper left')
plt.show()

#%%

#Exercicios

# 1) Calcule o erro da aproximação 

erro = la.norm(solEuler - solAnalitica)
print('Erro', erro)

# 2) Aumente o número de passos
# O erro diminuiu com o aumento do numero de passos

# 3) Gere um gráfico do erro em relação ao numero de passos (10^1 a 10^8)

_n = 10
p = 4
erros = []

for e in range(1, p):
    n = _n ** e
    
    dt = (tf - t0) / (n-1)
    t = np.linspace(t0, tf, n)
    a = np.zeros([n])
    
    #aplica condição inicial
    a[0] = a0
    
    #calcula metodo
    for i in range(1,n):
        a[i] = dt*(k*a[i-1])+a[i-1]
        
    #facilitador de leitura
    solEuler = a
    solAnalitica = a0*np.exp(k*t)
        
    erros.append(la.norm(solEuler - solAnalitica))
    
print(erros)

#plota graficos
#plt.plot(t, erros, 'r', label=u'Euler')
#plt.legend(loc='upper left')
#plt.show()