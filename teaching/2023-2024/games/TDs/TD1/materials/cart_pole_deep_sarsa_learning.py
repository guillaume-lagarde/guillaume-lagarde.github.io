import numpy as np
import gymnasium as gym
import pickle
import math

# goal: solve cart pole problem with monte carlo
env_name = "CartPole-v1"
env = gym.make(env_name, render_mode="human")
print(env.action_space)  # it is a discrete action space
print(env.action_space.n)  # number of actions
print(env.observation_space)  # it is a continuous state space


class DeepSarsaLearningAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        # Initialize weights near zero
        self.parameters = np.random.randn(4, 2) * 0.01
        self.gamma = 0.99
        self.epsilon = 0.1
        self.alpha = 0.1

    def play(self, observation):
        return np.random.choice(self.actions)

    def train(self, current_obs, action, reward, next_obs, done):
        pass


number_of_episodes = 50000  # number of episodes to train on
render_every = 1000  # render every 300 episodes

agent = DeepSarsaLearningAgent(env)  # create the agent

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