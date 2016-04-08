from numpy import *
from pylab import *

################################################################################
# Classes
################################################################################
class IzhNeuron:
  def __init__(self, label, a, b, c, d, v0, u0=None):
    self.label = label

    self.a = a
    self.b = b
    self.c = c
    self.d = d

    self.v = v0
    self.u = u0 if u0 is not None else b*v0


class IzhSim:
  def __init__(self, n, T, dt=0.25):
    self.neuron = n
    self.dt     = dt
    self.t      = t = arange(0, T+dt, dt)
    self.stim   = zeros(len(t))
    self.x      = 5
    self.y      = 140
    self.du     = lambda a, b, v, u: a*(b*v - u)

  def integrate(self, n=None):
    if n is None: n = self.neuron
    trace = zeros((2,len(self.t)))
    for i, j in enumerate(self.stim):
      n.v += self.dt * (0.04*n.v**2 + self.x*n.v + self.y - n.u + self.stim[i])
      n.u += self.dt * self.du(n.a,n.b,n.v,n.u)
      if n.v > 30:
        trace[0,i] = 30
        n.v        = n.c
        n.u       += n.d
      else:
        trace[0,i] = n.v
        trace[1,i] = n.u
    return trace

################################################################################
# Models
################################################################################
sims = []

# (A) Regular Spiking
n = IzhNeuron("(A) Regular Spiking", a=0.02, b=0.2, c=-65, d=2, v0=-70)
s = IzhSim(n, T=100)
for i, t in enumerate(s.t):
    s.stim[i] = 10 if t > 10 else 0
sims.append(s)


## (B) Intrinsically bursting
n = IzhNeuron("(B) Intrinsically bursting", a=0.02, b=0.2, c=-55, d=4, v0=-70)
s = IzhSim(n, T=150)
for i, t in enumerate(s.t):
    s.stim[i] = 10 if t > 10 else 0
sims.append(s)

## (C) Chattering
n = IzhNeuron("(C) Chattering", a=0.02, b=0.25, c=-50, d=2, v0=-70)
s = IzhSim(n, T=200)
for i, t in enumerate(s.t):
  s.stim[i] = 15 if t > 22 else 0
sims.append(s)



# (D) Fast Spiking
n = IzhNeuron("(D) Fast Spiking", a=0.1, b=0.2, c=-65, d=2, v0=-70)
s = IzhSim(n, T=200)
for i, t in enumerate(s.t):
  s.stim[i] = 10 if t > 20 else 0
sims.append(s)





## (E) Low-threshold spiking
n = IzhNeuron("(E) Low-threshold spiking", a=0.02, b=0.25, c=-65, d=2, v0=-62)
s = IzhSim(n, T=200)
for i, t in enumerate(s.t):
    s.stim[i] = 10 if t > 10 else 0
sims.append(s)










################################################################################
# Simulate
################################################################################
for i,s in enumerate(sims):
  res = s.integrate()


  #plt.suptitle('Classes of Inhibitory Cortical Cells')
  ax  = subplot(2, 3, i+1)

  ax.plot(s.t, res[0], s.t, -95 + ((s.stim - min(s.stim))/(max(s.stim) - min(s.stim)))*10)

  ax.set_xlim([0,s.t[-1]])
  ax.set_ylim([-100, 35])
  ax.set_title(s.neuron.label)
  #ax.set_xticklabels([])
  #ax.set_yticklabels([])
show()

