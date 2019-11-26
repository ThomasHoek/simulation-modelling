import numpy
import matplotlib.pyplot as plt

volume = 1000
num_steps = 1000

in_water = 6
out_water = 6

out_water2 = 5

h = in_water * 0.1

t = numpy.zeros(num_steps+1) # time
zout = numpy.zeros(num_steps+1) # zoutcontainer 1 ||| 6 in , 6 uit
zout2 = numpy.zeros(num_steps+1) # zout container 2 | 6 in , 5 uits
zout3 = numpy.zeros(num_steps+1) # zout met dx/dy?
zout4 = numpy.zeros(num_steps+1) # zout met dx/dy voor 5?


for step in range(num_steps):       # 6 in, 6 uit
    t[step+1] = t[step] + 1    
    zout[step+1] = (zout[step] + h) - (zout[step] /volume * out_water)


    a = h
    b = 1 / volume * out_water
    zout3[step+1] = zout3[step] + (a - b * zout3[step]) * h


volume2 = volume
volume2list = [volume2]

volume3 = volume
volume3list = [volume3]

for step in range(num_steps):       #  6 in, 5 uit.
    zout2[step+1] = (zout2[step] + h) - (zout2[step]/ volume2 * out_water2)

    volume2 = volume2 +  (in_water - out_water2)
    volume2list.append(volume2)


    a = h
    b = 1 / volume3 * out_water2 
    zout4[step+1] = zout4[step] + (a - b * zout4[step]) * h
    
    volume3 = volume3 + (in_water - out_water2)
    volume3list.append(volume3)



zoutPerVolume = [i / j for i, j in zip(zout2, volume2list)] 
zoutPerVolume2 = [i / j for i, j in zip(zout4, volume3list)] 


plt.plot(t,zout/volume,label="Zout 6 in, 6 uit")
plt.plot(t,zoutPerVolume,label="Zout 6 in, 5 uit")
plt.plot(t,zout3/volume,label="Zout 6 in, 6 uit, dx/dy")
plt.plot(t,zoutPerVolume2,label="Zout 6 in, 5 uit, dx/dy")
plt.legend()
plt.show()