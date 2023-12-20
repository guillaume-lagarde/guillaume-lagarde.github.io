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


class DeepQLearningAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        # We want to do linear function approximation, so we need to define the weights
        self.parameters = np.random.rand(4, 2)
        self.gamma = 0.99 # discount factor
        self.epsilon = 0.1 # exploration rate
        self.alpha = 1 # learning rate



    def play(self, observation):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            q_values_current_state = {action : np.dot(observation, self.parameters[:, action]) for action in self.actions}
            return max(q_values_current_state, key=q_values_current_state.get)
 

    def train(self, current_obs, action, reward, next_obs, done):
        if done:
            q_values_current_state_action = np.dot(current_obs, self.parameters[:, action])
            self.parameters[:, action] += self.alpha * (reward - q_values_current_state_action) * current_obs
            self.alpha = self.alpha * 0.9999
            print(self.parameters)
        q_values_current_state_action = np.dot(current_obs, self.parameters[:, action])
        q_values_next_state = {action : np.dot(next_obs, self.parameters[:, action]) for action in self.actions}
        self.parameters[:, action] += self.alpha * (reward + self.gamma * max(q_values_next_state.values()) - q_values_current_state_action) * current_obs
        # clip the parameters
        self.parameters = np.clip(self.parameters, -1000, 1000)

# def state_to_features(observation):
#     # extract some features from the observation for cartpole


class DeepSarsaLearningAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        # Initialize weights near zero
        self.parameters = np.random.randn(4, 2) * 0.01
        self.gamma = 0.99
        self.epsilon_start = 0.1
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.995
        self.epsilon = self.epsilon_start
        self.alpha_start = 0.1
        self.alpha_min = 0.01
        self.alpha_decay = 0.995
        self.alpha = self.alpha_start

    def play(self, observation):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            q_values_current_state = {action: np.dot(observation, self.parameters[:, action]) for action in self.actions}
            return max(q_values_current_state, key=q_values_current_state.get)

    def train(self, current_obs, action, reward, next_obs, done):
        q_values_current_state_action = np.dot(current_obs, self.parameters[:, action])
        q_values_next_state = {action: np.dot(next_obs, self.parameters[:, action]) for action in self.actions}
        # target = reward + self.gamma * max(q_values_next_state.values()) for q-learning
        target = reward + self.gamma * q_values_next_state[action]  # for sarsa
        
        if done:
            target = reward
        
        self.parameters[:, action] += self.alpha * (target - q_values_current_state_action) * current_obs
        self.parameters = np.clip(self.parameters, -2, 2)
        # self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        # self.alpha = max(self.alpha_min, self.alpha * self.alpha_decay)


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

with open("agent.pkl", "wb") as f:
    pickle.dump(agent, f)
