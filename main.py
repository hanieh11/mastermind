from modules.environment import Environment
from modules.player import Player

env = Environment(
    p1=Player(name='Hanieh')
)
env.launch_game(iterations=10)
