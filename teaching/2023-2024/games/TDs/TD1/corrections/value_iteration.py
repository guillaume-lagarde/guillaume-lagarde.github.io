from random import random
import numpy as np


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

# compute the transitions and rewards: no need to read it.
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
mdp = MDP(states, actions, transitions, rewards, bad_states)
mdp.print_grid()

print(" " * 50)
print(" " * 50)


# def value_iteration(mdp, gamma, epochs=100):
#     value = {state: 0 for state in mdp.states}
#     for _ in range(epochs):
#         for s in mdp.states:
#             value[s] = max(
#                 [
#                     sum(
#                         [
#                             mdp.transitions[(s, a, s2)]
#                             * (mdp.rewards[(s, a, s2)] + gamma * value[s2])
#                             for s2 in mdp.states
#                         ]
#                     )
#                     for a in mdp.actions
#                 ]
#             )
#     return value

def value_iteration(mdp, gamma, epochs=100):
    value = {state: 0 for state in mdp.states}
    for _ in range(epochs):
        for s in mdp.states:
            #print("=={0}======".format(s))
            maxVal = -float('inf')
            for a in mdp.actions:
                somme = 0
                for s2 in mdp.states:
                    somme += mdp.transitions[(s,a,s2)] * (mdp.rewards[(s,a,s2)] + gamma * value[s2])
                #print(somme)
                maxVal = max(maxVal, somme)
                #print("\t{0} {1}".format(action_to_symbol[a],maxVal))
            value[s] = maxVal
    return value

def derive_policy(mdp, value, gamma):
    policy = {state: 0 for state in mdp.states}
    for s in mdp.states:
        policy[s] = max(
            [
                (
                    sum(
                        [
                            mdp.transitions[(s, a, s2)]
                            * (mdp.rewards[(s, a, s2)] + gamma * value[s2])
                            for s2 in mdp.states
                        ]
                    ),
                    a,
                )
                for a in mdp.actions
            ]
        )[1]
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
