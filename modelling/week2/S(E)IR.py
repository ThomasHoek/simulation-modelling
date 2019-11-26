import numpy
import matplotlib.pyplot as plt

h = 0.05        # stap groote

population = 86 * (10 **7)
contacts = 70
infection_chance = 3

percentage_vaccinated = 45
vaccinated = population / 100 * percentage_vaccinated
transmission_cooef = contacts * (1/population) * (1/infection_chance)


latency_time = 2           # tijd van gezong naar infecteerd
infection_time = 6          # tijd om van geinfecteerd naar imuun te gaan

num_steps = 500

S = numpy.zeros(num_steps +1) # Gezond
E = numpy.zeros(num_steps +1) # Blootgesteld
I = numpy.zeros(num_steps +1) # Infecteerd
R = numpy.zeros(num_steps +1) # Imuun


S[0] = population - vaccinated
E[0] = 0
I[0] = 100
R[0] = vaccinated


for step in range(num_steps):
    # stap groote maal aantal mensen in de populatie, maal aantal geinfecteerden, maal vaste waarde aantal dat geinfecteerd wordt.
    s2e = h * transmission_cooef * S[step] * I[step]

    # bereken met de stapgroote na hoeveel dagen niet meer bloodgesteld is.
    e2i = h / latency_time * E[step]

    # bereken met de stapgroote na hoeveel dagen niet meer geinfecteerd is.
    i2r = h / infection_time* I[step]

    S[step + 1] = S[step] - s2e
    E[step + 1] = E[step] + s2e - e2i
    I[step + 1] = I[step] + e2i - i2r
    R[step+1] = R[step] + i2r


plt.plot(S,label = "Gezond")
plt.plot(E,label = "Blootgesteld")
plt.plot(I,label = "Infecteerd")
plt.plot(R,label = "Imuun")
plt.legend()

plt.show()

print(S)
# standarsized_infection_ratio = actual_number_of_infections / predicted_number_of_infections



