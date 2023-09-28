from random import random
import numpy as np
from utils import construct_frozen_lake


# goal here : solve frozen lake car problem with value iteration
# 1. implement value iteration
# 2. from the value function, derive the policy
# 3. run the policy on the environment


class MDP:
    """class for markov decision process"""

    def __init__(
        self, states=[], actions=[], transitions={}, rewards={}, bad_states=[]
    ):
        self.states = states
        self.actions = actions
        self.transitions = transitions  # a dictionary of type "{(s,a,s') : probability of the transition(s,a,s')}"
        self.rewards = rewards  # a dictionary of type "{(s,a,s') : reward of the transition(s,a,s')}"
        self.bad_states = bad_states

    def print_grid(self):
        for i in range(4):
            for j in range(4):
                if (i, j) in self.bad_states:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print("\n")


def valid_state(i, j):
    """check if a state is valid"""
    if i < 0 or i > 3 or j < 0 or j > 3:
        return False
    else:
        return True


# example frozen-lake
states = [(i, j) for i in range(4) for j in range(4)]
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
transitions = {(s, a, s2): 0 for s in states for a in actions for s2 in states}
rewards = {(s, a, s2): 0 for s in states for a in actions for s2 in states}
bad_states = [(1, 0), (2, 0)]
final_state = (3, 3)
# we call construct_frozen_lake to fill the transitions and rewards dictionaries
construct_frozen_lake(valid_state, states, actions, transitions, rewards, bad_states, final_state)
mdp = MDP(states, actions, transitions, rewards, bad_states)
mdp.print_grid()

print(" " * 50)
print(" " * 50)


def value_iteration(mdp, gamma, epochs=100):
    value = {state: 0 for state in mdp.states}
    # TODO
    return value


def derive_policy(mdp, value, gamma):
    policy = {state: (0,1) for state in mdp.states}
    # TODO
    return policy


def print_policy_on_grid(mdp, policy, gamma):
    action_to_symbol = {(0, 1): "→", (0, -1): "←", (1, 0): "↓", (-1, 0): "↑"}
    for i in range(4):
        for j in range(4):
            if (i, j) in mdp.bad_states:
                print("X", end=" ")
            else:
                print(action_to_symbol[policy[(i, j)]], end=" ")
        print("\n")


# test
value = value_iteration(mdp, 0.9)
policy = derive_policy(mdp, value, 0.9)
print_policy_on_grid(mdp, policy, 0.9)
