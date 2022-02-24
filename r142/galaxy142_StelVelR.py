#galaxy 142 Ray's stellar velocity maps
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody_velmaps.scripts.plot_manga_velmaps import *

filename='/mnt/data0/jillian/gguaman/r142/cosmo25p.768sg1bwK1BHe75.007779'
redshift=0.03
image_width=20

stellar_map, ax = plot_star_map(filename, redshift, image_width, orientation="sideon")
#stellar_pa = calc_pa(stellar_map)

#plt.show()
plt.savefig("galaxy142_StelVelMap.png")
#plt.savefig("galaxy142_StelVelMapR(side).png")
