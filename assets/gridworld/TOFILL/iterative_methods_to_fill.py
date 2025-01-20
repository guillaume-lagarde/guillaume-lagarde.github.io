from grid_world import GridWorldMDP
import pprint as pp

GAMMA = 0.9

gridworld = GridWorldMDP(10, 10, 30)

def policy_evaluation(gridworld: GridWorldMDP, policy, num_iterations=100):
    value_policy = {state: 0 for state in gridworld.states}
    # TODO: Implement the function
    return value_policy

def value_iteration(gridworld: GridWorldMDP, num_iterations=100) -> dict:
    '''Compute the optimal value function for the given gridworld'''
    optimal_values = {state: 0 for state in gridworld.states}
    # TODO: Implement the function
    return optimal_values

def get_policy_from_value_function(gridworld: GridWorldMDP, value_function: dict) -> dict:
    '''Compute the optimal policy given the value function'''
    policy = {state: (1,0) for state in gridworld.states}
    # TODO: Implement the function
    return policy

optimal_values = value_iteration(gridworld, num_iterations=100)
gridworld.print_value_function(optimal_values)
optimal_policy = get_policy_from_value_function(gridworld, optimal_values)
gridworld.print_policy(optimal_policy)