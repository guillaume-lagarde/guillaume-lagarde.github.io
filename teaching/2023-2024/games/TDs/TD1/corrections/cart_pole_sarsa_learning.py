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


class SarsaLearningAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        self.states = range(162)  # number of states
        self.q_values = {
            (s, a): 0 for s in self.states for a in self.actions
        }  # dictionary of type "{(s,a) : q_value}"
        self.gamma = 0.99  # discount factor
        self.epsilon = 1
        self.alpha = 1
        self.total_reward = 0
        self.episode_number = 0

    def get_epsilon(self, episode_number):
        """ Return the epsilon (exploration rate) for the given episode number """
        min_epsilon = 0.1
        return max(min_epsilon, min(1, 1 - math.log10((episode_number + 1) / 25)))

    def get_alpha(self, episode_number):
        """ Return the alpha (learning rate) for the given episode number """
        min_alpha = 0.1
        return max(min_alpha, min(1, 1 - math.log10((episode_number + 1) / 25)))


    def play(self, observation):
        state = discretization_cartpole(observation)
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            q_values_current_state = {
                action: self.q_values[state, action] for action in self.actions
            }
            return max(q_values_current_state, key=q_values_current_state.get)

    def train(self, current_obs, action, reward, next_obs, done):
        self.total_reward += reward
        if not done:
            state = discretization_cartpole(current_obs)
            next_state = discretization_cartpole(next_obs)
            # self.q_values[state, action] += (
            #     self.alpha
            # ) * (
            #     reward
            #     + self.gamma * max(
            #         [self.q_values[next_state, a] for a in self.actions]
            #     )
            #     - self.q_values[state, action]
            # ) # Q-Learning
            next_action = self.play(next_obs)
            self.q_values[state, action] += (
                self.alpha
            ) * (
                reward
                + self.gamma * self.q_values[next_state, next_action]
                - self.q_values[state, action]
            )
        else:
            state = discretization_cartpole(current_obs)
            self.q_values[state, action] += self.alpha * (reward - self.q_values[state, action])
            self.episode_number += 1
            self.epsilon = self.get_epsilon(self.episode_number)
            self.alpha = self.get_alpha(self.episode_number)

            self.total_reward = 0



number_of_episodes = 50000  # number of episodes to train on
render_every = 1000  # render every 300 episodes

agent = SarsaLearningAgent(env)  # create the agent

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

with open("agent.pkl", "wb") as f:
    pickle.dump(agent, f)