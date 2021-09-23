#making pictures pynbody tutorials: velocity vectors
import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt

#loading snapshot
s = pynbody.load('/mnt/data0/jillian/gguaman/cptmarvel.5.std')

#setting to physical units
s.physical_units()

#centering halos
pynbody.analysis.angmom.faceon(s)

#creating subplots
f, axs = plt.subplots(1,2,figsize=(14,6))

#creating slice showing gas temp, with velocity vectors overlaid
sph.velocity_image(s.g,vector_color="cyan",qty="temp",width=50,denoise=True,approximate_fast=False,subplot=axs[0],show_cbar=False)

#making stream visualization instead of quiver plot
pynbody.analysis.angmom.faceon(s)
s['pos'].convert_units('Mpc')
sph.velocity_image(s.g,width='3 Mpc',cmap="Greys_r", mode='stream',units='Msol kpc^-2',density=2.0,vector_resolution=100,vmin=1e-1,subplot=axs[1],show_cbar=False,vector_color='black')

#plt.show()
plt.savefig("cptmarvel_velvecs.png")
