#galaxy 109 GG Gas velocity code
import pynbody
import numpy as np
import pynbody.plot.sph as sph
import matplotlib.pyplot as plt

def stars_sideon(
    h,
    vec_to_xform=pynbody.analysis.angmom.calc_sideon_matrix,
    cen_size="1 kpc",
    disk_size="5 kpc",
    cen=None,
    vcen=None,
    move_all=True,
    **kwargs
):
    """

    Reposition and rotate the simulation containing the halo h to see
    h's disk edge on.

    Given a simulation and a subview of that simulation (probably the
    halo of interest), this routine centers the simulation and rotates
    it so that the disk lies in the x-z plane. This gives a side-on
    view for SPH images, for instance.

    """
    from pynbody import transformation, filt
    from pynbody.analysis import halo

    global config

    if move_all:
        top = h.ancestor
    else:
        top = h

    # Top is the top-level view of the simulation, which will be
    # transformed

    if cen is None:
        # or h['pos'][h['phi'].argmin()]
        cen = halo.center(h, retcen=True, **kwargs)

    tx = transformation.inverse_translate(top, cen)

    if vcen is None:
        vcen = halo.vel_center(h, retcen=True, cen_size=cen_size)

    tx = transformation.inverse_v_translate(tx, vcen)

    # Use stars from inner 10kpc to calculate angular momentum vector
    if len(h.s) > 0:
        cen = h.s[filt.Sphere(disk_size)]
    else:
        cen = h[filt.Sphere(disk_size)]

    trans = vec_to_xform(pynbody.analysis.angmom.ang_mom_vec(cen))

    tx = transformation.transform(tx, trans)

    return tx

#s=pynbody.load('/mnt/data0/jillian/gguaman/cosmo25p.768sg1bwK1BHe75.008192')
s=pynbody.load('/mnt/data0/jillian/gguaman/r109/r107.007779.tipsy')

#setting to physical units
s.physical_units()

#centering halo
#pynbody.analysis.angmom.faceon(s)
#pynbody.analysis.angmom.sideon(s)
stars_sideon(s)

#creating star velocity plot
sph.image(s.g,qty="vz",width='30 kpc',cmap="RdBu", log=False, units='km s**-1',vmin=-150, vmax=150)

#function to find BH
def findBH(s):
    BHfilter=pynbody.filt.LowPass('tform',0.0)
    BH=s.stars[BHfilter]
    return BH
BH=findBH(s)
print("The number of black holes is:",len(BH))

BHposition = BH['pos']
#print("The black hole's postion is", BHposition)
print("The BHs position is",BH['pos'].in_units('kpc'))

for i in range(len(BH)):
    #putting BH x in column
    BHx=BHposition[[i],0]
   #putting BH y in column
    BHy=BHposition[[i],1]
   #putting BH z in column
    BHz=BHposition[[i],2]
    plt.plot(BHx,BHy, 'ro')
    
#plt.show()
plt.savefig("galaxy109_GasVelGG.png")
