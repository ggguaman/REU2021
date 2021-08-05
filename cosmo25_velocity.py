#cosmo 25 gas velocity code
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')
s.physical_units()

#centering halo
pynbody.analysis.angmom.sideon(s)

#creating gas velocity plot
sph.image(s.g,qty="vr",denoise=True,approximate_fast=False,log=False)

plt.show()
#plt.savefig("cosmo25_velocity.png")
