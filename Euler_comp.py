from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from time import time

tic = time()

lam = 0.5
y0 = 2

T = 10
N = 100
dt = T/N
t = np.arange(0,(T+dt),dt)

EEsol = [y0]
EIsol = [y0]
Hsol = [y0]


for i in np.arange(0,len(t)-1):
    ans1 = EEsol[i] + dt*lam*EEsol[i]
    EEsol.append(ans1)

    ans2 = EIsol[i]/(1 - dt*lam)
    EIsol.append(ans2)

    ans3 = Hsol[i] + dt*lam*Hsol[i]
    fans3 = Hsol[i] + (dt/2)*(lam*Hsol[i]+lam*ans3)
    Hsol.append(fans3)

toc=time()
t_sim = toc-tic
print(t_sim)

plt.figure(0)
plt.plot(t, EEsol)
plt.plot(t, EIsol)
plt.plot(t, Hsol)
plt.plot(t, 2*np.exp(lam*t))
plt.show()


