import numpy
import matplotlib.pyplot as plt

i_tank1 = 6

o_tank1_i_tank2 = 3
i_tank1_o_tank2 = 1

o_tank1 = 4
o_tank2 = 2

volume = 100
num_steps = 250

t = numpy.zeros(num_steps+1) # time
zout_tank1 = numpy.zeros(num_steps+1) # zoutcontainer 1 ||| 6 in , 6 uit
zout_tank2 = numpy.zeros(num_steps+1) # zout container 2 | 6 in , 5 uits
zout_tank3 = numpy.zeros(num_steps+1) 

zout_tank1[0] = 0
zout_tank2[0] = 20 


for step in range(num_steps):
    h = 0.2 * i_tank1
    t[step+1] = t[step] + 1

    in_tank1 = 0.2 * i_tank1
    out_tank1 = 1/volume * zout_tank1[step] * o_tank1
    in_tank1_out_tank2 = 1/volume * zout_tank2[step] * i_tank1_o_tank2

    out_tank1_to_tank2 = 1/volume * zout_tank1[step] * o_tank1_i_tank2
    out_tank2 = 1/volume * zout_tank2[step] * o_tank2

    zout_tank1[step+1] = zout_tank1[step] - out_tank1 - out_tank1_to_tank2 + in_tank1_out_tank2 + in_tank1
    zout_tank2[step+1] = zout_tank2[step] - out_tank2 + out_tank1_to_tank2 - in_tank1_out_tank2 
    
    

print(zout_tank1[-1]/(volume *2 ))
plt.plot(zout_tank1/volume)
plt.plot(zout_tank2/volume)
plt.show()