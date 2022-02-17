#galaxy 320 Ray's gas velocity maps
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody_velmaps.scripts.plot_manga_velmaps import *

filename='/mnt/data0/jillian/gguaman/r320/cosmo25p.768sg1bwK1BHe75.007779'
redshift=0.05
image_width=20

gas_map, ax = plot_gas_map(filename, redshift, image_width, orientation="sideon")

plt.show()
