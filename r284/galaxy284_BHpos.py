#galaxy 284 BH postion
import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pynbody import filt, array

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r284/cosmo25p.768sg1bwK1BHe75.007779')

#setting physical units
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
    #print([s],['pos'])

BHposition = BH['pos']
print("The black hole's postion is", BHposition)
print(BH['pos'].in_units('kpc'))

#putting BH x in column
BHx=BHposition[[0],0]
print(BHx)

#putting BH y in column
BHy=BHposition[[0],1]
print(BHy)

#putting BH z in column
BHz=BHposition[[0],2]
print(BHz)
