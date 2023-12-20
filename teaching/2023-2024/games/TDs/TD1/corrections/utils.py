import numpy as np


def discretization_cartpole(observation):
    x, x_dot, theta, theta_dot = observation

    # Convert angles to degrees for the comparison
    theta = np.degrees(theta)
    theta_dot = np.degrees(theta_dot)

    # Constants in degrees
    twelve_degrees = 12.0
    six_degrees = 6.0
    one_degree = 1.0
    fifty_degrees = 50.0

    # Check failure cases
    if x < -2.4 or x > 2.4 or theta < -twelve_degrees or theta > twelve_degrees:
        return -1

    # Discretize the x value
    if x < -0.8:
        box = 0
    elif x < 0.8:
        box = 1
    else:
        box = 2

    # Discretize the x_dot value
    if x_dot >= -0.5 and x_dot < 0.5:
        box += 3
    elif x_dot >= 0.5:
        box += 6

    # Discretize the theta value
    if theta >= -six_degrees and theta < -one_degree:
        box += 9
    elif theta >= -one_degree and theta < 0:
        box += 18
    elif theta >= 0 and theta < one_degree:
        box += 27
    elif theta >= one_degree and theta < six_degrees:
        box += 36
    elif theta >= six_degrees:
        box += 45

    # Discretize the theta_dot value
    if theta_dot >= -fifty_degrees and theta_dot < fifty_degrees:
        box += 54
    elif theta_dot >= fifty_degrees:
        box += 108

    return box
