#galaxy 168 stars code
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s=pynbody.load('/mnt/data0/jillian/gguaman/r168/cosmo25p.768sg1bwK1BHe75.007779')

#setting to physical units
s.physical_units()

#centering halo
pynbody.analysis.angmom.faceon(s)

#creating image using default bands(i,v,u)
pynbody.plot.stars.render(s,width='18 kpc')

#plt.show()
plt.savefig("galaxy168_stars.png")
