from random_generator import RNG
import matplotlib.pyplot as plt
import math

random1 = RNG(seed= 5812, num_steps= 10000)
random2 = RNG(seed = 315, num_steps= 10000)



z0a = [math.sqrt(-2.0 * math.log(x)) for x in random1]
z0b = [math.cos(math.tau * y) for y in random2]

z1a = [math.sqrt(-2.0 * math.log(x)) for x in random1]
z1b =  [math.sin(math.tau * y) for y in random2]

z0 = [a*b for a,b in zip(z0a,z0b)]
z1 = [a*b for a,b in zip(z1a,z1b)]

fig, ax = plt.subplots(3)
ax[0].scatter(x=z0,y=z1)
ax[1].hist(z0,bins = 100)
ax[2].hist(z1,bins = 100)
plt.show()