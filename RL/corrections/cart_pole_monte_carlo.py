import numpy as np
import gymnasium as gym
import pickle
from utils import discretization_cartpole

# goal: solve cart pole problem with monte carlo
env_name = "CartPole-v1"
env = gym.make(env_name, render_mode="human")
print(env.action_space)  # it is a discrete action space
print(env.action_space.n)  # number of actions
print(env.observation_space)  # it is a continuous state space


class MonteCarloAgent:
    def __init__(self, env):
        self.env = env
        self.actions = range(env.action_space.n)
        self.states = range(162)  # number of states
        self.q_values = {
            (s, a): 0 for s in self.states for a in self.actions
        }  # dictionary of type "{(s,a) : q_value}"
        self.number_of_visits = {
            (s, a): 0 for s in self.states for a in self.actions
        }  # dictionary of type "{(s,a) : number of visits}"
        self.gamma = 0.99  # discount factor
        self.epsilon = (
            1  # exploration rate, start with 1 and then decrease it over time
        )
        self.episode = []

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
        self.episode.append((current_obs, action, reward))
        if done:
            self.update_q_values()
            self.episode = []
            self.epsilon = self.epsilon * 0.99  # decrease exploration rate over time

    def update_q_values(self):
        T = len(self.episode)
        G = 0
        for i in range(T - 1, -1, -1):
            current_obs, action, reward = self.episode[i]
            state = discretization_cartpole(current_obs)
            self.number_of_visits[state, action] += 1
            G = self.gamma * G + reward
            self.q_values[state, action] += (
                1 / self.number_of_visits[state, action]
            ) * (G - self.q_values[state, action])


number_of_episodes = 5000  # number of episodes to train on
render_every = 100  # render every 300 episodes

agent = MonteCarloAgent(env)  # create the agent

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
