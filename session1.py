#__author__ = 'samuel'

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def current(px, x_in, x_out, zx):
    v = np.linspace(-100*10**(-3),100*10**(-3),1000)
    f = 9.648*(10**4)
    r = 8.314
    t = 279.45
    y = ((px*(zx**2)*(f**2)*v)/(r*t))*(x_in-x_out*np.exp(((-zx)*f*v)/(r*t)))\
    /(1-np.exp(((-zx)*f*v)/(r*t)))
    return y


def plot_element(*elements):
    v = np.linspace(-100*10**(-3),100*10**(-3),1000)
    dict = {1: 'K', 2: 'Na', 3: 'Cl'}
    for element in elements:
        for key in dict:
            if element == dict[key] and key == 1:
                y = current(0.01, 0.4*(10**(-6)), 0.02*(10**(-6)), 1)
                plt.plot(v, y, color = 'blue', label = 'K')
                plt.draw()
            elif element == dict[key] and key == 2:
                y = current(0.0003, 0.05*(10**(-6)), 0.44*(10**(-6)), 1)
                plt.plot(v, y, color = 'red', label = 'Na')
                plt.draw()
            elif element == dict[key] and key == 3:
                y = current(0.001, 0.04*(10**(-6)), 0.56*(10**(-6)), -1)
                plt.plot(v, y, color = 'green', label = 'Cl')
                plt.draw()
    plt.legend(loc='upper right')
    plt.ylabel('Current')
    plt.xlabel('Membrane potential')
    plt.show()

#plot_element('Na','Cl','K')



def plot_mix(*elements):
    v = np.linspace(-100*10**(-3),100*10**(-3),1000)
    dict = {1: 'K', 2: 'Na', 3: 'Cl'}
    for element in elements:
        for key in dict:
            if element == dict[key] and key == 1:
                y = current(0.01, 0.4*(10**(-6)), 0.02*(10**(-6)), 1)
                plt.plot(v, y, color = 'blue', label = 'K')
                plt.draw()
            elif element == dict[key] and key == 2:
                y = current(0.0003, 0.05*(10**(-6)), 0.44*(10**(-6)), 1)
                plt.plot(v, y, color = 'red', label = 'Na')
                plt.draw()
            elif element == dict[key] and key == 3:
                y = current(0.001, 0.04*(10**(-6)), 0.56*(10**(-6)), -1)
                plt.plot(v, y, color = 'green', label = 'Cl')
                plt.draw()
    y1 = current(0.01, 0.4*(10**(-6)), 0.02*(10**(-6)), 1)
    y2 = current(0.0003, 0.05*(10**(-6)), 0.44*(10**(-6)), 1)
    y3 = current(0.001, 0.04*(10**(-6)), 0.56*(10**(-6)), -1)
    final_y = y1+y2+y3
    plt.plot(v, final_y, color = 'purple', label = 'mix')
    plt.draw()
    plt.legend(loc='upper right')
    plt.ylabel('Current')
    plt.xlabel('Membrane potential')
    plt.show()



#plot_mix('Na','Cl','K')









def fit(element, gx):
    v = np.linspace(-100*10**(-3),100*10**(-3),1000)
    if element == 'K':
        ex = -0.072
        y = current(0.01, 0.4*(10**(-6)), 0.02*(10**(-6)), 1)
        y1 = gx*(v-(ex))  #straight line
        plt.plot(v, y, color = 'blue', label = 'K')
        plt.plot(v, y1, color = 'black', label = 'fitted line')
    elif element == 'Na':
        ex = 0.052
        y = current(0.0003, 0.05*(10**(-6)), 0.44*(10**(-6)), 1)
        y1 = gx*(v-(ex))  #straight line
        plt.plot(v, y, color = 'red', label = 'Na')
        plt.plot(v, y1, color = 'black', label = 'fitted line')
    elif element == 'Cl':
        ex = -0.064
        y = current(0.001, 0.04*(10**(-6)), 0.56*(10**(-6)), -1)
        y1 = gx*(v-(ex))  #straight line
        plt.plot(v, y, color = 'green', label = 'Cl')
        plt.plot(v, y1, color = 'black', label = 'fitted line')
    plt.legend(loc='upper right')
    plt.draw()
    plt.show()


#fit('Cl', 0.00633)



def rc_circuit():
    a =1; cm =1; te = 1 ; ie=10 ; rm=1 ; em=-70
    t0 = np.linspace(0,1,1000)
    v = em + ((rm*ie)/a)*(1-np.exp(-t0/(rm*cm)))
    plt.plot(t0,v, color='blue')
    plt.draw()
    t1 = np.linspace(1,10,1000)
    v2 = em + (v[-1]-em)*np.exp(-(t1-te)/rm*cm)
    plt.plot(t1, v2, color='red')
    plt.draw()
    plt.show()

rc_circuit()