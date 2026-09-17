# grid_game.py
import random


class GridHuntGame:
    """A small Pacman-style grid environment (4x4) where an agent collects food."""

    
#Environment is __init__
    def __init__(self, width=4, height=4):      # width=4, height=4 - defining Grid dimensions, This is the small, non-visual environment (GridHuntGame) from Lab 01. It's telling Python: "unless someone says otherwise, make this grid 4 columns wide and 4 rows tall." It's a tiny 4×4 board — good for quick console-based testing, not meant to be pretty or fast to visualize.
        self.width = width    # Width of the grid (number of columns), Without this, width would just be a local variable inside __init__ that disappears once the constructor finishes.
        self.height = height   # Height of the grid (number of rows)
        self.agent_pos = [0, 0]  # Agent's starting position (x, y)

        # Place a few random food pellets and obstacles (walls)
        # Stored as a set of (x, y) tuples so "is my position here?" checks are fast.
        # (A set cannot hold lists, because lists are changeable / unhashable.)
        self.food_positions = {(1, 2), (2, 3), (3, 0), (2, 1)}
        self.walls = {(1, 1), (2, 2)}

        self.score = 0
        self.steps = 0

    def get_percept(self, agent) -> dict:
        return {
            'agent_pos': list(self.agent_pos),
            'smells_food': tuple(self.agent_pos) in self.food_positions,
            'hit_wall': tuple(self.agent_pos) in self.walls,
            'score': self.score,
            'remaining_food': len(self.food_positions)
            

        }

    def execute_action(self, agent, action: str):
        self.steps += 1
        new_pos = list(self.agent_pos)

        if action == 'Up':
            new_pos[1] = min(self.height - 1, new_pos[1] + 1)
        elif action == 'Down':
            new_pos[1] = max(0, new_pos[1] - 1)
        elif action == 'Left':
            new_pos[0] = max(0, new_pos[0] - 1)
        elif action == 'Right':
            new_pos[0] = min(self.width - 1, new_pos[0] + 1)

        # Check collision with walls
        if tuple(new_pos) in self.walls:
            self.score -= 5  # Penalty for hitting a wall
        else:
            self.agent_pos = new_pos

        # Check if eating food
        tuple_pos = tuple(self.agent_pos)
        if tuple_pos in self.food_positions:
            self.food_positions.remove(tuple_pos)
            self.score += 20  # Reward for eating food pellet

    def is_done(self) -> bool:
        return len(self.food_positions) == 0 or self.steps >= 20