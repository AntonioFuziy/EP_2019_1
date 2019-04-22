import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
'''
d1=0.1
d2=0.05
def g(T1):
    if T1<=150:
        Q=0
    else:
        Q=14
    return Q
def f(T2,t):
    if t<80:
        y=0
    else:
        y=d2*T2
    return y

Tmax =200
delta_t = 0.001
lista_tempo = np.arange(0,Tmax,delta_t)

def EquacoesDiferenciais(lista_solucoes,t):
    T1=lista_solucoes[0]
    T2=lista_solucoes[1]
    funcao1 = g(T1)
    funcao2 = f(T2,t)
    dT1dt = -d1*T1 + funcao1
    dT2dt = d1*T1 - funcao1 - funcao2
    return [dT1dt,dT2dt]

s0=[300,0]
solucao = odeint(EquacoesDiferenciais, s0, lista_tempo)

plt.plot(lista_tempo,solucao[:,0])
plt.plot(lista_tempo,solucao[:,1])
plt.grid(True)
plt.show()



T1 = [300]
T2 = [0]
cont = 0

def EquacoesDiferenciais(T1,T2,t):
    funcao1 = g(T1)
    funcao2 = f(T2, t)
    dT1dt = -d1 * T1 + g(T1)
    dT2dt = d1 * T1 - g(T1) - f(T2,t)
    return [dT1dt, dT2dt]

while cont<len(lista_tempo):
    dT1dt, dT2dt = EquacoesDiferenciais(T1[cont], T2[cont], lista_tempo[cont])
    T1.append(T1[cont] + (dT1dt)*delta_t)
    T2.append(T2[cont] + (dT2dt)*delta_t)
    cont+=1
plt.plot(lista_tempo,T1[0:-1])
plt.plot(lista_tempo,T2[0:-1])
plt.grid(True)
plt.show()'''


def f(t):
    y=t**2
    return y


Tmax=10
delta_t=0.01
lista_tempo=np.arange(0,Tmax,delta_t)
t=lista_tempo

plt.plot(lista_tempo,f(lista_tempo))
plt.grid(True)
plt.show()

def derivada_t(t,delta_t):



