import numpy
import matplotlib.pyplot as plt

num_steps = 100
h = 1/num_steps
x = numpy.zeros(num_steps+2)
y = numpy.zeros(num_steps+2)
heun = numpy.zeros(num_steps+2)

y[0] = 1    
heun[0] = 1
for step in range(num_steps+1):
    x[step+1] = (step + 1) * h
    y[step+1] = y[step] * (h+1)
    
    fTime =x[step+1] - x[step]
    fHeun = heun[step] - heun[step-1]
    huenslope1 = fTime / fHeun
    huenslope2 = (fTime + h) / (fHeun + huenslope1 * h)
    heun[step+1] = heun[step] + (0.5 * huenslope1  + 0.5* huenslope2) * h


    

plt.plot(x, y)
plt.plot(x, heun)

print(y[-1])
print(heun[-1])
plt.show()