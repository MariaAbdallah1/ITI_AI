import random

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Starting position at (0, 0)
        self.visited = set()   # To log visited positions

    def __str__(self) -> str:
        return f"Agent at position {self.position} in environment {self.environment}"

    def random_movement(self):
        # Randomly choose an action: move left, move right, move up, move down
        actions = ['left', 'right', 'up', 'down']
        action = random.choice(actions)

        if action == 'left' and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif action == 'right' and self.position[0] < self.environment.width - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif action == 'up' and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif action == 'down' and self.position[1] < self.environment.height - 1:
            self.position = (self.position[0], self.position[1] + 1)

        # Clean if there's dirt
        if self.environment.is_dirty(self.position):
            self.environment.clean(self.position)
            print(f"Agent cleaned dirt at position {self.position}")

    def ModelThinking_Movemnt(self):
        directions = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        # Check the current position
        if self.environment.is_dirty(self.position):
            self.environment.clean(self.position)
            print(f"Agent cleaned dirt at position {self.position}")
            self.visited.add(self.position)

        # Check adjacent cells
        for direction, (dx, dy) in directions.items():
            new_position = (self.position[0] + dx, self.position[1] + dy)
            if (0 <= new_position[0] < self.environment.width and
                0 <= new_position[1] < self.environment.height and
                new_position not in self.visited):

                if self.environment.is_dirty(new_position):
                    self.position = new_position
                    self.environment.clean(self.position)
                    print(f"Agent moved to and cleaned dirt at position {self.position}")
                    self.visited.add(self.position)
                    return  # Return immediately after cleaning to ensure only one action per call

        # If no dirty adjacent cells, choose a random position if not all cells are visited
        if len(self.visited) < self.environment.width * self.environment.height:
            while True:
                self.random_movement()
                if self.position not in self.visited:
                    break

            print(f"Agent moved to random position {self.position}")
            self.visited.add(self.position)

    def run(self, steps=10):
        for _ in range(steps):
            print(f"Agent is at position {self.position}")
            self.ModelThinking_Movemnt()

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(height)] for _ in range(width)]  # Initialize grid with no dirt

    def add_dirt(self, position):
        self.grid[position[0]][position[1]] = True

    def clean(self, position):
        self.grid[position[0]][position[1]] = False

    def is_dirty(self, position):
        return self.grid[position[0]][position[1]]

    def print_grid(self):
        for row in self.grid:
            print(row)

env = Environment(width=5, height=5)
env.add_dirt((1, 1))
env.add_dirt((2, 3))
env.print_grid()
agent = VacuumAgent(environment=env)
agent.run(steps=10)
env.print_grid()
