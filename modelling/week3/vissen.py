import matplotlib.pyplot as plt
import numpy

maximum_growth_rate = 0.5 # 1 / year
carrying_capacity = 2e6 # tons
maximum_harvest_rate = 0.7 * 2.5e5 # tons / year
ramp_start = 2. # years
ramp_end = 6. # years

end_time = 10. # years
h = 0.1 # years
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def harvest():
    fish = numpy.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    is_extinct = False
    for step in range(num_steps):
        time = h * step
        harvest_factor  = 0.0
        if time > ramp_end:
            harvest_factor = 1.0
        elif time > ramp_start:
            harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)
        harvest_rate = harvest_factor * maximum_harvest_rate

        if is_extinct:
            fish_next_step = 0.
        else:
            fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
            if fish_next_step <= 0.:
                is_extinct = True
                fish_next_step = 0.
        fish[step + 1] = fish_next_step

    return fish

fish = harvest()


plt.plot(times, fish)
plt.show()


