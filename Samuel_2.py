"""
@author: Samuel Mensah

We solve the 2-d Fitzhugh-Nagumo model for spiking neurons

dv/dt = v-(v^3/3)-w+I, I is the current
dw/dt = eps(b0+b1v-w)

or written as
dY/dt = F(Y,t)

where Y = [v,w]
and  F(Y,t) = [v-(v^3/3)-w+I, eps(b0+b1v-w)]

"""

from pylab import *
import numpy as np
from scipy.integrate import odeint


"""Values of the parameters"""
eps = 0.1; b0 = 2
b1 = 1.5; I = 2 #vary values of I

"""initial conditions"""
Y0 = [-3,-1]

"""define ODEs"""
def f(Y,t,p):
    vdot = Y[0]-((Y[0]**3)/3) - Y[1] + p[3]
    wdot = p[0]*(p[1] + (p[2]*Y[0]) - Y[1])
    return [vdot, wdot]

"""Parameters to pass to ODE"""
p = [eps, b0, b1, I]

"""Time to simulate system over"""
t = np.linspace(0,50,100)

"""Solve system"""
Y = odeint(f, Y0, t, args=(p,))

"""plot system against time"""
#To plot solutions: hush out lines 46,47 & 53
# plt.plot(t, Y[:,0], color ='red')
# plt.plot(t, Y[:,1], color ='blue')
plt.legend()
plt.xlabel('Time')
plt.ylabel('FHN Parameters')
plt.legend(loc='upper right')
plt.title('Fitzhugh-Nagumo Model')
#plt.show()



"""Plot Trajectory on Phase Diagram"""
plt.plot(Y[:,0],Y[:,1])
plt.legend()
plt.xlabel('dV')
plt.ylabel('dW')
plt.title('Fitzhugh-Nagumo Solution Trajectory')

x = np.linspace(-3,3,10)
y = np.linspace(-5,5,10)

(X,Y) = meshgrid(x,y)
dV = X-((X**3)/3) - Y + p[3]
dW = p[0]*(p[1] + (p[2]*Y[0]) - Y)

Q = quiver( X, Y, dV, dW)
plt.grid()
plt.show()

