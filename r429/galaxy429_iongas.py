#galaxy 429 ionized gas code
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph	as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r429/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)

#filter to only use ionised gas
GasFilter = pynbody.filt.HighPass('temp','15848 K')

#creating image to show velocity of ionised gas
sph.image(s.g[GasFilter],qty="vr",vmin=-20,width=40,denoise=True,approximate_fast=False,log=False)

#plt.show()
plt.savefig("galaxy429_iongas.png")
