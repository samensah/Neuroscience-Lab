'''
@author: Samuel Mensah

We solve the 2-d Dynamical System and show that
a limit cycle exists around (0,0) for the following
dynamical system

dx/dt = x - y - x^3
dy/dt = x + y - y^3

or written as

dY/dt = F(Y,t)

where Y = [x,y]
and  F(Y,t) = [x-y-x^3, x+y-y^3]

'''
from pylab import *
import numpy as np
from scipy.integrate import odeint


"""initial conditions"""
Y0= [-3,-1]

"""define ODEs"""
def f(Y,t):
    xdot = Y[0]-Y[1]-(Y[0]**3)
    ydot = Y[0]+Y[1]-(Y[1]**3)
    return [xdot, ydot]


"""Time to simulate system over"""
t = np.linspace(0,10,100)

"""Solve system"""
Y = odeint(f,Y0,t)

"""plot system"""
plt.plot(t, Y[:,0], color ='red')
plt.plot(t, Y[:,1], color ='blue')
plt.legend()
plt.xlabel('Time')
plt.ylabel('FHN Parameters')
plt.legend(loc='upper right')
plt.title('Fitzhugh-Nagumo Model')
plt.show()



plt.plot(Y[:,0],Y[:,0])













x = np.linspace(-10,10,10)
y = np.linspace(-50,50,10)


(X,Y) = meshgrid(x,y)
dX = X - Y - (X**3)
dY = X + Y - (Y**3)

#1
Q = quiver( X, Y, dX, dY)
#plt.plot()


plt.show()


