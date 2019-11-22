import numpy
import matplotlib.pyplot

def forward_euler():
    h=0.1           # time steps
    g=9.81          # gravity
    friction = 0.02
    s = -0.1

    num_steps = 1000
    t = numpy.zeros(num_steps+1) # time
    x = numpy.zeros(num_steps+1) # position 
    v = numpy.zeros(num_steps+1) # velocity

    x[0] = 5

    for step in range(num_steps):
        t[step+1] = t[step] + h
        v[step+1] = v[step] + s * x[step] - v[step] * friction * h
        x[step+1] = x[step] + v[step+1] * h 
        
    return t,x,v

t,x,v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()

plot_me()