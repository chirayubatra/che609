from numpy import zeros
from random import choice, uniform
import matplotlib.pyplot as plt
from math import log, factorial

row = 
col = 
n = 
num_steps = 

def initialize(row,col,n):
    """Given lattice parameters and number of particles, this function should return a list of all particle positions.
    Initially you want all the particles to be gathered along the left edge of the system."""
    return positions_of_particles


def possible_transitions(positions_of_particles):
    """Given a list of all particle coordinates, the function should return a list of all possible transitions."""
    return possible_transitions


def perform_Transition(positions_of_particles):
    """Given a list of all particle coordinates, the function should pick a valid transition and return an updated list of particle coordinates.
    This function should run the Possible transitions-function and choose a transition based on the transition list that is returned. Use the choice function that has been imported. This function randomly picks an element from a list, assuming a flat distribution.
    from random import choice
    Chosen transition = choice(List of transitions)
    Having selected a transition, use list comprehension to update the particle positions’ list.
    """
    return positions_of_particles


def entropy_calc(positions_of_particles, row, col, n):
    """Given a list of all particle coordinates and the initial parameters, the func- tion should calculate the local entropy of the set of particles.

    Local entropy is, in the context of this exercise and only for illustrative purposes, defined as the entropy of the particle system as it spreads out over an area. Consider n particles on a lattice. Now imagine a rectangle just large enough to encompass all of those particles. The total number of lattice sites encompassed by this rectangle define the local number of available lattice sites, Nlocal. The entropy may now be calculated using the multiplicity definition of entropy.

    S/kb = ln(Nlocal! / n!(Nlocal − n)!)

    """
    return log(factorial(lattice_spread)/(factorial(n)*factorial(lattice_spread - n)))

def create_image(positions_of_particles, tr_num): 
    """Given a list of all particle coordinates, the function creates a correspond- ing numpy array to visualise the lattice and creates an image file that is saved in the local folder. Such a system can be modelled using a numpy array and letting the array sites take the values 0 and 1. 
    A 0 represents an empty lattice site, and a 1 represents a site occupied by a particle.
    The necessary image-plotting code is already added to this function. You need to write the code that creates the array that the image is created from.

    Args:
        positions_of_particles ([type]): [description]
        tr_num ([type]): [description]
    """
    # tr_num keeps track of the step number in the loop. You will have to define this variable outside of this function.
    # Create the array here
    imgplot = plt.imshow(current_state, cmap='binary')
    plt.savefig('Lattice' + str(tr_num) + '.png')



if __name__ == "__main__":
        
    # Use the initialize function to create a list of all the particles positions

    # Remember to set up lists for the time stamp and the local entropy that can be updated inside the loop


    # Start the loop. Both a for-loop and a while-loop will work.
        # Remember to store an image at a regular interval. Use if tr_num % 100 == 0:
        # Update the positions_of_particles-list using perform_Transition()
        # Update the entropy and time-step list. Make sure that the time step list reflects the total time passed at any given point.
        # If using a while-loop, update tr_num


    # The code below creates the plots the local entropy as a function of time.
    plt.clf()
    plt.plot(time_step, local_entropy)
    plt.show()