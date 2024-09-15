from collections import defaultdict
from pprint import pprint
import numpy as np
import tqdm
import logging
import pickle

logging.basicConfig(level=logging.INFO)

DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY = 20, 20 # number of discretized states for position and velocity
NUM_ITERATIONS = 1000 # number of iterations for value iteration
NUMBER_OF_SAMPLES = 20 # number of samples to compute transition probabilities
GAMMA = 0.99 # discount factor

class MDP:
    def __init__(self, discretization=(DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY), num_samples=NUMBER_OF_SAMPLES, gamma=GAMMA):
        self.gamma = gamma
        self.discretization = discretization
        self.discretization_position = discretization[0]
        self.discretization_velocity = discretization[1]
        self.number_of_samples = num_samples
        
        self.states = {(i, j) for i in range(self.discretization_position) for j in range(self.discretization_velocity)}
        self.actions = [0, 1, 2]

        logging.info("Computing transition probabilities")
        self.transition_probabilities = self.compute_transition_probabilities()
        logging.info("Transition probabilities computed")

        logging.info("Computing rewards")
        self.rewards = self.compute_rewards()
        logging.info("Rewards computed")

    def compute_transition_probabilities(self):
        transition_probabilities = defaultdict(lambda: 0)
        # TODO: Implement the computation of the transition probabilities
        return transition_probabilities
    
    def compute_rewards(self):
        rewards = defaultdict(lambda: -1)
        # TODO: Implement the computation of the rewards
        return rewards
    

# Now that we have defined the MDP of the mountain car problem, we can use Value Iteration to solve it

def value_iteration(mdp, num_iterations=NUM_ITERATIONS):
    V = {state: 0 for state in mdp.states}
    # TODO: Implement the value iteration algorithm
    return V

def get_policy(mdp, V):
    policy = {}
    # TODO: Implement the computation of the policy
    return policy


if __name__ == "__main__":
    logging.info("Computing MDP")
    mdp = MDP()
    logging.info("MDP computed")

    logging.info("Computing Value Iteration")
    V = value_iteration(mdp)
    logging.info("Value Iteration computed")

    logging.info("Computing policy")
    policy_mountain_car = get_policy(mdp, V)
    logging.info("Policy computed")

    # save policy to file using pickle
    with open("policy.pkl", "wb") as f:
        pickle.dump(policy_mountain_car, f)




