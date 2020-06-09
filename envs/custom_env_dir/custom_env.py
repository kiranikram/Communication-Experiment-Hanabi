import gym

class HanabiEnv(gym.Env):

	def __init__(self):
		print('Env initialized')

	def step(self):
		print('Step success!')

	def reset(self):
		print('Env reset!')
