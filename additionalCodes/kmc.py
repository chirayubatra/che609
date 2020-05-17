from random import uniform #will be used to pick random numbers between 0 and 1
from math import log
import matplotlib.pyplot as plt # will be used to create the relevant plots


#Part 1
N_a = # number of particles of type A
N_b = # number of particles of type B
N_c = # number of particles of type C

k_f = # kinetic forward constant
k_r = # kinetic reverse constant



def probability_forward(k_f, k_r, n_a, n_b, n_c): 
    """Calculates the probability of a forward transition. NOTE: the reverse probability is 1 - forward."""
    return 


num_trans = #Sets up transition counter
equilibrium = False #Sets up equilibrium check
n_a_time = #Sets up vector describing number of A particles
n_b_time = #Sets up vector describing number of B particles
n_c_time = #Sets up vector describing number of C particles
time_step = #Sets up vector describing the time passed after each transitions
while not equilibrium:
    if # Use uniform(0,1) (generates random number) to select either forward or reverse reaction
        # Update the particle counts acording to the reaction equation
    else: # If the random number is higher than forward probability, the reverse transition is picked
        # Update the particle counts according to the reaction equation

    # Remember to update your parameters as the simulation runs, for plotting.

    # Remember to add an equilibrium condition to change equilibrium from False to True if equilibrium has been reached.


#Part 3
#SHow plot of number of each particle as a function of time. plt.plot(x-axis, y-axis, color)
plt.plot(, , 'r')
plt.plot(, , 'b')
plt.plot(, , 'g')
plt.show()

