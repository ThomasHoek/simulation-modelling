import numpy
import matplotlib.pyplot as plt

h=0.3
num_steps = 10
time = numpy.zeros(num_steps+1)
euler = numpy.zeros(num_steps+1)
heun = numpy.zeros(num_steps+1)

euler[0] = 1
heun[0] = 1

for step in range(num_steps):  
    time[step+1] = time[step]

    fTime = time[step+1] - time[step]
    fEuler = euler[step] - euler[step-1]
    fHeun = heun[step] - heun[step-1]

    euler[step+1] = euler[step] + h * (fTime/fEuler)


    huenslope1 = fTime / fHeun
    huenslope2 = (fTime + h) / (fHeun + huenslope1 * h)
    heun[step+1] = heun[step] + (0.5 * huenslope1  + 0.5* huenslope2) * h
    
#   y+1 = yn  + h/2  f(xn,yn) + f(xn + h , yn + h * f(xn, yn))
#   huen+1 = huen[n]  + h/2  f(time[n],huen[n]) + f(huen[n] + h , huen[n] + h * f(time[n], huen[n]))


axes_height = plt.subplot(221)
plt.plot(time, time)
plt.title("Time plus steps H")

axes_height = plt.subplot(222)
plt.plot(time, time)
plt.plot(time, euler)
plt.title("Time and forward Euler Method")

axes_height = plt.subplot(223)
plt.plot(time, time)
plt.plot(time, heun)
plt.title("Time and heun Method")

axes_height = plt.subplot(224)
plt.plot(time, time)
plt.plot(time, euler)
plt.plot(time, heun)
plt.title("Time and Euler and Heun")
plt.show()    