"""
Solving the RC ODE equation:
C_m dV/dt = (E_m-V)/R_m+I_e/a

We are using I_e a step function Ie=`0 0<t<5, then I_e=0 for t>=5
C_m, R_m, a are all parameters and E_m is the resting potential
"""


from __future__ import division
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

"""Define RHS of ODE"""

def f(V,t,p):
    Em = p[0]
    Rm = p[1]
    Cm = p[2]
    Ie = p[3]
    a = p[4]
    return (Em-V)/(Rm*Cm)+Ie/(Cm*a)

"""Constants"""
Em = -70; Rm = 1; Ie = 10
a = 1; Cm = 1; te = 5

"""Put constants together"""
p = [Em, Rm, Cm, Ie, a]


"""Initial Conditions"""
V0 = Em

"""Time"""
t = np.linspace(0, 10, 100)

"""Solve ODE"""
V = odeint(f, V0, t, args=(p,))

"""Plot Solution"""
plt.plot(t, V)
plt.show()