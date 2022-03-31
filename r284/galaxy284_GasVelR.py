#galaxy 284 Ray's gas velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody_velmaps.position_angles import *
from pynbody_velmaps.scripts.plot_manga_velmaps import *

filename='/mnt/data0/jillian/gguaman/r284/cosmo25p.768sg1bwK1BHe75.007779'
#filename= '/mnt/data0/jillian/gguaman/r284/r284.007779.tipsy'
redshift=0.03
image_width=30

def rho_sq(particles):
    return particles['rho']**2

gas_map, gas_pa, ax = plot_manga_map(filename, redshift, "gas", weights=rho_sq,image_width=image_width, orientation="sideon", cmap='RdBu',vmin=-150, vmax=150)

#plt.show()
plt.savefig("galaxy284_GasVelR.png")