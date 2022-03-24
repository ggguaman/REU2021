#galaxy 429 Ray's stellar velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody_velmaps.scripts.plot_manga_velmaps import *
from pynbody_velmaps.position_angles import *

filename='/mnt/data0/jillian/gguaman/r429/cosmo25p.768sg1bwK1BHe75.007779'
#filename = '/mnt/data0/jillian/gguaman/r429/r429.007779.tipsy'
redshift=0.01
image_width=30

stellar_map, stellar_pa, ax = plot_manga_map(filename, redshift, "star", weights="mass", image_width=image_width, orientation="sideon", cmap='PuOr', vmin=-70, vmax=70)

#plt.show()
plt.savefig("galaxy429_StelVelR.png")
