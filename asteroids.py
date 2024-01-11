import gymnasium as gym


#returns an environment for users to interact with
env = gym.make('ALE/Asteroids-v5', render_mode = 'human')     #create environment and how it should be visualized
observation, info = env.reset()     #reset the environment to start

for env_spec in gym.envs.registry.all():
    if env_spec.id.startswith("ALE/"):
        print(env_spec.id, env_spec.entry_point, env_spec.kwargs)


for _ in range(1000):
    action = env.action_space.sample()      #set random actions
    observation, reward, terminated, truncated, info = env.step(action)     #agent performs an action and receives info/reward back

    if terminated or truncated:     #conditions to reset the environment again
        observation, info = env.reset()


env.close()