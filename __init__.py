from .envs import CassieEnv
from gym.envs.registration import register

register(
    id='Cassie-v1',
    entry_point='cassie.envs:CassieEnv',
)
