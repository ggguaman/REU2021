#galaxy 330 gas velocity code
import pynbody
import numpy as np
import pandas as pd
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r330/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
#pynbody.analysis.angmom.faceon(s)
pynbody.analysis.angmom.sideon(s)

#creating gas velocity plot
sph.image(s.g,qty="vr",width=40,denoise=True,approximate_fast=False,log=False)

#plt.show()
#plt.savefig("galaxy330_velocity.png")
plt.savefig("galaxy330_velocity(side).png")
