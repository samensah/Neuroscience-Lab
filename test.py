#__author__ = 'samuel'


from __future__ import division
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
"""
Created on Wed Feb 25 13:57:47 2015



Example of use of odeint for system of equations.
Here we solve the HH model

dx/dt = ax-bxy
dy/dt = cxy - dy

or written as

dY/dt = F(Y,t)

where Y = [x,y]
and F(Y,t) = [ax-bxy,cxy-dy]

"""


"""define ODEs"""
def am(v):
    return 0.1*(v+40)/(1-np.exp(-(v+40)/10))

def an(v):
    return 0.01*(v+55)/(1-np.exp(-(v+55)/10))

def ah(v):
    return 0.07*np.exp(-(v+65)/20)

def bm(v):
    return 4*np.exp(-(v+65)/18)

def bn(v):
    return 0.125*np.exp(-(v+65)/80)

def bh(v):
    return 1/(1+np.exp(-(v+35)/10))

def Ie(t):
    return 2


def f(Y, t, p):
    vdot = p[0]*Y[1]**3*Y[3]*(p[3]-Y[0])+p[1]*Y[2]**4*(p[4]-Y[0])+p[2]*(p[5]-Y[0])+Ie(t)
    mdot = am(Y[0])*(1-Y[1])-bm(Y[0])*Y[1]
    ndot = an(Y[0])*(1-Y[2])-bn(Y[0])*Y[2]
    hdot = ah(Y[0])*(1-Y[3])-bh(Y[0])*Y[3]
    return [vdot, mdot, ndot, hdot]

"""initial conditions"""

Y0 = [-65, am(-65)/(am(-65)+bm(-65)), an(-65)/(an(-65)+bn(-65)), ah(-65)/(ah(-65)+bh(-65))]
print(Y0)


"""Values of the parameters"""


gn = 120
gk = 36
gl = 0.3
ENa = 50
EK = -77
El = -54.4


"""Lump parameters together to pass to ODE"""

p = [gn, gk, gl, ENa, EK, El]

"""Time to simulate system over"""
t = np.linspace(0, 100, 5000)

"""Solve system"""
Y = odeint(f, Y0, t, args=(p, ))

"""plot system"""
plt.plot(Y[:,2], Y[:,3])
plt.show()
plt.plot(t, Y[:,0],'r',label='Voltage')
plt.legend()
plt.xlabel('Time')
plt.ylabel('V')
plt.show()
plt.plot(t, Y[:,1], 'b', label='m')
plt.plot(t, Y[:,2], 'r', label='n')
plt.plot(t, Y[:,3], 'y', label='h')
plt.legend()
#plt.xlabel('Time')Lotka Volterra model
plt.ylabel('V')
#plt.title('Lotka Volterra model of predator-prey system')
plt.show()