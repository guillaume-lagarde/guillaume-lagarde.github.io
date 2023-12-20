import numpy as np
import gymnasium as gym
import pickle
import math
from utils import discretization_cartpole

# goal: solve cart pole problem with monte carlo
env_name = "CartPole-v1"
env = gym.make(env_name, render_mode="human")
print(env.action_space)  # it is a discrete action space
print(env.action_space.n)  # number of actions
print(env.observation_space)  # it is a continuous state space


class QLearningAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        self.states = range(162)  # number of states
        self.q_values = {
            (s, a): 0 for s in self.states for a in self.actions
        }  # dictionary of type "{(s,a) : q_value}"
        self.gamma = 0.99  # discount factor
        self.epsilon = 0.1 # exploration rate
        self.alpha = 0.1 # learning rate

    def play(self, observation):
        return np.random.choice(self.actions)

    def train(self, current_obs, action, reward, next_obs, done):
        pass



number_of_episodes = 50000  # number of episodes to train on
render_every = 1000  # render every 300 episodes

agent = QLearningAgent(env)  # create the agent

for i, episode in enumerate(range(number_of_episodes)):
    print("episode ", i)
    done = False

    if i % render_every == 0:
        if render_every != 1:
            env = gym.make(env_name, render_mode="human")
    else:
        env = gym.make(env_name, render_mode="rgb_array")

    obs, _ = env.reset()

    while not done:
        action = agent.play(obs)
        next_obs, reward, done, truncated, _ = env.step(action)
        agent.train(obs, action, reward, next_obs, done)
        obs = next_obs

# store the agent

# with open("agent.pkl", "wb") as f:
#     pickle.dump(agent, f)
