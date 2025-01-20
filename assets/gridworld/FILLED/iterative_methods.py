from grid_world import GridWorldMDP
import pprint as pp

GAMMA = 0.9

gridworld = GridWorldMDP(10, 10, 10)


def policy_evaluation(gridworld: GridWorldMDP, policy, num_iterations=100):
    value_policy = {state: 0 for state in gridworld.states}
    for _ in range(num_iterations):
        for state in gridworld.states:
            action = policy[state]
            value_policy[state] = sum([gridworld.transition_probabilities[(state, action, new_state)]*(gridworld.rewards[state, action, new_state] + GAMMA*value_policy[new_state]) for new_state in gridworld.states])
    return value_policy

def value_iteration(gridworld: GridWorldMDP, num_iterations=100) -> dict:
    '''Compute the optimal value function for the given gridworld'''
    optimal_values = {state: 0 for state in gridworld.states}
    for _ in range(num_iterations):
        for state in gridworld.states:
            optimal_values[state] = max([sum([gridworld.transition_probabilities[(state, action, new_state)]*(gridworld.rewards[state, action, new_state] + GAMMA*optimal_values[new_state]) for new_state in gridworld.states]) for action in gridworld.actions])
    return optimal_values

def get_policy_from_value_function(gridworld: GridWorldMDP, value_function: dict) -> dict:
    '''Compute the optimal policy given the value function'''
    policy = {}
    for state in gridworld.states:
        policy[state] = max(gridworld.actions, key=lambda action: sum([gridworld.transition_probabilities[(state, action, new_state)]*(gridworld.rewards[state, action, new_state] + GAMMA*value_function[new_state]) for new_state in gridworld.states]))
    return policy



optimal_values = value_iteration(gridworld, num_iterations=100)
gridworld.print_value_function(optimal_values)
optimal_policy = get_policy_from_value_function(gridworld, optimal_values)
gridworld.print_policy(optimal_policy)

