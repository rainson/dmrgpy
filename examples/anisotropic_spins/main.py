# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
import spinchain
n = 3
for i in range(1):
  spins = [np.random.randint(2,6) for i in range(n)] # spin 1/2 heisenberg chain
  sc = spinchain.Spin_Chain(spins) # create the spin chain
  def fj(i,j): 
      m = np.random.random((3,3))
#      return m
#      return m + m.transpose()
#      m *= 0.0
#      m[0,1] = 1.0
#      m[1,0] = -1.0
      return m
  def fb(i): return np.random.random(3)
  sc.set_exchange(fj)
  sc.set_fields(fb)
  e0 = sc.gs_energy(mode="DMRG") # compute the ground state energy
  e1 = sc.gs_energy(mode="ED") # compute the ground state energy
  print("Spin chain",spins)
  print("Energy with ED",e1)
  print("Energy with DMRG",e0)
  print("\n")
  de = np.abs(e1-e0)
  if de>0.1: raise
print("Test passed")











