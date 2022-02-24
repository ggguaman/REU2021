#galaxy 320 Ray's stellar velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody_velmaps.scripts.plot_manga_velmaps import *
from pynbody_velmaps.position_angles import *

#filename='/mnt/data0/jillian/gguaman/r320/cosmo25p.768sg1bwK1BHe75.007779'
filename = '/mnt/data0/jillian/gguaman/r320/r320.007779.tipsy'
redshift=0.01
image_width=20

stellar_map, ax = plot_manga_map(filename,redshift,"star",image_width,orientation="sideon")
#stellar_pa = calc_pa(stellar_map)
#plt.colorbar(ax.images[0])
#plt.xlabel('x/kpc')
#plt.ylabel('y/kpc')

plt.show()
#plt.savefig("galaxy320_StelVelR.png")
