from queue import PriorityQueue
from PIL import Image, ImageDraw

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1 or contents.count("B") != 1:
            raise Exception("Maze must have exactly one start point and one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i, line in enumerate(contents):
            row = []
            for j, char in enumerate(line):
                if char == "A":
                    self.start = (i, j)
                    row.append(False)
                elif char == "B":
                    self.goal = (i, j)
                    row.append(False)
                elif char == " ":
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

        self.solution = None
        self.num_explored = 0
        self.explored = set()  # Add explored set

    def print(self):
        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, cell in enumerate(row):
                if cell:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        directions = [("up", (row - 1, col)), ("down", (row + 1, col)), ("left", (row, col - 1)), ("right", (row, col + 1))]
        return [(action, (r, c)) for action, (r, c) in directions if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]]

    def manhattan_distance(self, state):
        return abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])

    def solve(self, algorithm):
        self.num_explored = 0
        self.explored = set()
        start = Node(state=self.start, cost=0, heuristic=self.manhattan_distance(self.start))
        priority_queue = PriorityQueue()
        priority_queue.put((start.cost + start.heuristic, start))

        while not priority_queue.empty():
            _, node = priority_queue.get()

            if node.state == self.goal:
                self.solution = self._reconstruct_path(node)
                return

            if node.state not in self.explored:
                self.num_explored += 1
                self.explored.add(node.state)

                for action, state in self.neighbors(node.state):
                    if state not in self.explored and not any(n.state == state for _, n in priority_queue.queue):
                        cost = node.cost + 1
                        heuristic = self.manhattan_distance(state)
                        child = Node(state=state, parent=node, action=action, cost=cost, heuristic=heuristic)
                        if algorithm == 'gbfs':
                            priority_queue.put((heuristic, child))
                        else:  # A*
                            priority_queue.put((cost + heuristic, child))

    def _reconstruct_path(self, node):
        actions, cells = [], []
        while node.parent:
            actions.append(node.action)
            cells.append(node.state)
            node = node.parent
        actions.reverse()
        cells.reverse()
        return (actions, cells)

    def output_image(self, filename, show_solution=True, show_explored=False):
        cell_size = 50
        cell_border = 2
        img = Image.new("RGBA", (self.width * cell_size, self.height * cell_size), "black")
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, cell in enumerate(row):
                fill = self._get_color(i, j, solution, show_solution, show_explored)
                draw.rectangle(
                    [(j * cell_size + cell_border, i * cell_size + cell_border),
                     ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)],
                    fill=fill
                )

        img.save(filename)

    def _get_color(self, i, j, solution, show_solution, show_explored):
        if self.walls[i][j]:
            return (40, 40, 40)
        if (i, j) == self.start:
            return (255, 0, 0)
        if (i, j) == self.goal:
            return (0, 171, 28)
        if solution and show_solution and (i, j) in solution:
            return (220, 235, 113)
        if show_explored and (i, j) in self.explored:
            return (212, 97, 85)
        return (237, 240, 252)

def main():
    maze = Maze("c:/Users/Maria Abdallah/Downloads/Maria_iti/day 3/maze2.txt")

    print("Maze:")
    maze.print()

    print("Solving with A*...")
    maze.solve('astar')
    print("A* Path:")
    maze.print()
    print("States Explored A*:", maze.num_explored)
    maze.output_image("c:/Users/Maria Abdallah/Downloads/Maria_iti/day 4/maze_astar.png", show_explored=True)

    print("Solving with Greedy Best-First Search...")
    maze.solve('gbfs')
    print("GBFS Path:")
    maze.print()
    print("States Explored GBFS:", maze.num_explored)
    maze.output_image("c:/Users/Maria Abdallah/Downloads/Maria_iti/day 4/maze_gbfs.png", show_explored=True)

if __name__ == "__main__":
    main()
