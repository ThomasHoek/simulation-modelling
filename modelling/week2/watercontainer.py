import numpy
import matplotlib.pyplot as plt

volume = 1000
num_steps = 2000

in_water = 6
out_water = 6
out_water2 = 5

h = in_water * 0.1

t = numpy.zeros(num_steps+1) # time
zout = numpy.zeros(num_steps+1) # zout
zout2 = numpy.zeros(num_steps+1) # zout2


for step in range(num_steps):
    t[step+1] = t[step] + 1    
    zout[step+1] = (zout[step] + h) - (zout[step] /volume * out_water)


volume2 = volume
volume2list = [volume2]

for step in range(num_steps):
    zout2[step+1] = (zout2[step] + h) - (zout2[step]/ volume2 * out_water2)
    volume2 = volume2 + (out_water2 - in_water)
    volume2list.append(volume2)
    


zoutPerVolume = [i / j for i, j in zip(zout2, volume2list)] 


plt.plot(t,zout/volume)
plt.plot(t,zoutPerVolume)
plt.show()