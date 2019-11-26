import numpy
import matplotlib.pyplot as plt


num_steps = 10
h = 1/num_steps

t = numpy.zeros(num_steps+1) # time
euler = numpy.zeros(num_steps+1) # euler
heun = numpy.zeros(num_steps+1) # euler

euler[0] = 1
heun[0] = 1
for step in range(num_steps):
    t[step+1] = t[step] + h
    euler[step+1] = euler[step] + euler[step] *  h

    leftheun = heun[step]
    rightheun = heun[step] +h

    heun[step+1] = heun[step] + h* (leftheun + rightheun)/2
    # https://image.slidesharecdn.com/nmfirstsecond-180726082016/95/heuns-method-5-638.jpg?cb=1532593353


print(euler[-1])
print(heun[-1])
plt.plot(t,euler)
plt.plot(t,heun)
plt.show()