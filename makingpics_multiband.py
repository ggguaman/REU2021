#pynbody tutorial: multiband image
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)

#creating image using default bands(i,v,u)
pynbody.plot.stars.render(s,width='10 kpc')

#plt.show()
plt.savefig("cptmarvel_stars.png")
