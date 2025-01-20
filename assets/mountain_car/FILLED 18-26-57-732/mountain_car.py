import pickle
import gymnasium as gym
import tqdm
env = gym.make('MountainCar-v0', render_mode="human")

## stupid agent = always push right
class StupidAgent:
    def __init__(self, env):
        self.env = env
    def act(self, observation):
        return 2


from mdp_mountain_car import MDP, discretize, DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY

with open("policy_mountain_car.pkl", "rb") as f:
    policy_mount_car = pickle.load(f)


class OptimalAgent:
    def __init__(self, env):
        self.env = env
    def act(self, observation):
        position, velocity = observation
        state = discretize(position, velocity, (DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY))
        return policy_mount_car[state]
    

agent = OptimalAgent(env)
for i in range(10):
    observation, info = env.reset()
    for i in tqdm.tqdm(range(1000)):
        action = agent.act(observation)
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            break