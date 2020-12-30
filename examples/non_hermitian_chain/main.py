# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np
from dmrgpy import fermionchain
n = 8
fc = fermionchain.Fermionic_Chain(n) # create the fermion chain
mh = np.zeros((n,n),dtype=np.complex) # TB matrix
for i in range(n-1):
    mh[i,i+1] = 1.0
    mh[i+1,i] = 1.0
for i in range(n): mh[i,i] = 1j*0.2*(-1)**i
h = 0 # initialize Hamiltonian
for i in range(n):
    for j in range(n):
        h = h + mh[i,j]*fc.Cdag[i]*fc.C[j]
for i in range(n-1): h = h + (fc.N[i]-0.5)*(fc.N[i+1]-0.5)
from dmrgpy import mpsalgebra
# the GS mode targets the state with minimum Re(E)

fc.set_hamiltonian(h)
print(fc.get_excited(mode="ED"))  ; exit()

wfs = mpsalgebra.mpsarnoldi(fc,h,mode="GS",n=5,nwf=5,verbose=1)
es = np.array([wf.dot(h*wf) for wf in wfs]) # energies
wf = [y for (x,y) in sorted(zip(es.real,wfs))][0] # lowest energy

print("MPS Energy",wf.dot(h*wf))
import scipy.linalg as lg
es = lg.eigvals(mh) # eigenvalues
print("Exact TB energy",np.sum(es[es.real<0.0]))
