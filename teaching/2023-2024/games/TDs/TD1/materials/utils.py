import numpy as np

# compute the transitions and rewards: no need to read it.
def construct_frozen_lake(valid_state, states, actions, transitions, rewards, bad_states, final_state):
    for s in states:
        for a in actions:
            if s == final_state:
                rewards[(s, a, s)] = 0
                transitions[(s, a, s)] = 1
            else:
                exact_neighbor = (
                [(s[0] + a[0], s[1] + a[1])]
                if valid_state(s[0] + a[0], s[1] + a[1])
                else [s]
            )
                slipped_neighbors = [
                (s[0] + a2[0], s[1] + a2[1])
                for a2 in actions
                if a2 != a and valid_state(s[0] + a2[0], s[1] + a2[1])
            ]
                for s2 in exact_neighbor:
                    transitions[(s, a, s2)] = 0.9
                    if s2 in bad_states:
                        rewards[(s, a, s2)] = -10
                    else:
                        rewards[(s, a, s2)] = 0
                for s2 in slipped_neighbors:
                    if s2 in bad_states:
                        rewards[(s, a, s2)] = -10
                    else:
                        rewards[(s, a, s2)] = 0
                    transitions[(s, a, s2)] = 0.1 / len(slipped_neighbors)

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
