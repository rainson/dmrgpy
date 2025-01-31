# Add the root path of the dmrgpy library
import os ; import sys ; sys.path.append(os.getcwd()+'/../../src')

import numpy as np # conventional numpy library
from dmrgpy import spinchain # library dealing with DMRG for spin chains
import matplotlib.pyplot as plt # library to plot the results
####################################
### Create the spin chain object ###
####################################
n = 10 # total number of spins
spins = [2 for i in range(n)] # list with the different spins of your system
# the spins are labeled by 2s+1, so that 2 means s=1/2, 3 meand S=1 ....
sc = spinchain.Spin_Chain(spins) # create the spin chain object



##############################
### Create the hamiltonian ###
##############################
def fj(i,j): # function to define the exchange couplings
    if abs(i-j)==1: return 1.0  # first neighbors
    else: return 0.0 # otherwise
sc.set_exchange(fj) # add the exchange couplings
#sc.set_fields(fb) # optionally you could add local magnetic fields
# parameters controlling the DMRG algorithm, in principle default ones are fine
sc.cutoff = 1e-10 # cutoff
sc.maxm = 30 # bond dimension
sc.nsweeps = 5 # number of sweeps
############################################################
# Perform ground state calculation and compute correlators #
############################################################
# compute ground state energy
e0 = sc.gs_energy() # compute ground state energy



# this array constains the pairs of spins on which you want to compute
# <GS|S_i S_j GS>
pairs = [(0,i) for i in range(n)] # between the edge and the rest
cs = sc.get_correlator(pairs) # get the static correlators
# save the result in a file
np.savetxt("CORRELATOR.OUT",np.matrix([range(n),cs]).T)
########################
# Now plot the results #
########################
# now plot the result
import matplotlib
matplotlib.rcParams.update({'font.size': 18})
matplotlib.rcParams['font.family'] = "Bitstream Vera Serif"
fig = plt.figure()
fig.subplots_adjust(0.2,0.2)
plt.plot(range(n),cs,marker="o")
plt.xlabel("N")
plt.ylabel("<GS|S_0 S_N |GS>")
plt.show()











