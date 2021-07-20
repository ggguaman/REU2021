#finding black hole position
import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

#loading snapshot
s = pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')
s.physical_units
#h=s.halos()
#function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
with pynbody.analysis.halo.center(s, mode='hyb'):
    print([s],['pos'])

BHposition = BH['pos']
print("The black hole's postion is", BHposition)
print(BH['pos'].in_units('kpc'))
