# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:57:47 2015

@author: emma

Example of use of odeint for system of equations. 
Here we solve the Lotka-Volterra system for predator (y), prey (x)

dx/dt = ax-bxy
dy/dt = cxy - dy

or written as

dY/dt = F(Y,t)

where Y = [x,y]
and  F(Y,t) = [ax-bxy,cxy-dy]

"""
from __future__ import division
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

"""define ODEs"""
def f(Y,t,p):
    xdot = p[0]*Y[0]-p[1]*Y[0]*Y[1]
    ydot = p[2]*Y[0]*Y[1] - p[3]*Y[1]
    return [xdot,ydot]

"""initial conditions"""
Y0=[12,5]

"""Values of the parameters"""
a= 3
b= 1.5
c= 2
d= 2

p=[a,b,c,d] #Lump parameters together to pass to ODE

"""Time to simulate system over"""
t = np.linspace(0,30,300)

"""Solve system"""
Y = odeint(f,Y0,t,args=(p,))

"""plot system"""
plt.plot(t, Y[:,0],'r',label='Prey')
plt.plot(t, Y[:,1],'b',label='Predator')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Poulation numbers')
plt.title('Lotka Volterra model of predator-prey system')


x1 = np.linspace(0,10,10)
y1 = np.linspace(0,10,10)
b0 = 2 ; b1 = 1.5 ; eps = 0.1 ; I = 0

(X,Y) = meshgrid(x1, y1)

figure()
xdot = p[0]*Y[0]-p[1]*Y[0]*Y[1]
ydot = p[2]*Y[0]*Y[1] - p[3]*Y[1]
Q = quiver( X, Y, xdot, ydot)


plt.show()
