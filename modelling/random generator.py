import numpy as np
import matplotlib.pyplot as plt
import math

def monte_carlo_pi():
    pi_list = []
    
    x = RNG(seed = 841)
    y = RNG(seed = 204)

    # plt.scatter(x,y,s=0.1,c = (x**2 + y**2)<1)
    # plt.show()

    pi_list = [(x_curr, y_curr) for x_curr, y_curr in zip(x, y)]

    
    pi_list = [1 if (x**2 + y**2) < 1 else 0 for (x,y) in pi_list]
        
    
    return (sum(pi_list)/ len(pi_list)) * 4



def RNG(a = 421, c = 291, m = 100000, seed = 715, num_steps = 100000):
    RNG_list = np.zeros(num_steps+1) # time
    RNG_list[0] = seed
    if (m > 0) and (a < m) and (c < m) and (seed < m):
        for i in range(num_steps):
            RNG_list[i + 1] = (a * RNG_list[i] + c) % m 

            
        return RNG_list/m
    else:
        return False


def plot():
    return_lst = RNG()
    print(sum(return_lst)/ len(return_lst))
    return_lst.sort()
    plt.hist(return_lst, bins=100000)
    plt.show()


pi = monte_carlo_pi()
print("Difference is: " , abs(math.pi - pi))
print("Calculated pi:", pi)

# plot()