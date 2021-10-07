#galaxy 168 BH position
import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r142/cosmo25p.768sg1bwK1BHe75.007779')

s.physical_units()

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is",len(BH))

#distance BH is from galaxy
#with pynbody.analysis.halo.center(s, mode='hyb'):
print([s],['pos'])

BHposition = BH['pos']
print("The black hole's postion is", BHposition)

print(BH['pos'].in_units('kpc'))
