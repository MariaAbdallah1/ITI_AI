from queue import PriorityQueue

class PuzzleState:
    def __init__(self, board, parent=None, move=None, g=0, heuristic=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g
        self.heuristic = heuristic

    def f(self):
        return self.g + self.heuristic

    def __lt__(self, other):
        return self.f() < other.f()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return None

def manhattan_distance(board, goal):
    distance = 0
    goal_flat = [tile for row in goal for tile in row]  # Flatten the goal state
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_x, goal_y = divmod(goal_flat.index(board[i][j]), 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def misplaced_tiles(board, goal):
    misplaced_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                misplaced_count += 1
    return misplaced_count

def generate_neighbors(state, goal, heuristic_func):
    neighbors = []
    empty_x, empty_y = state.find_empty()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in state.board]
            new_board[empty_x][empty_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[empty_x][empty_y]
            g = state.g + 1  # Cost to reach the neighbor
            heuristic = heuristic_func(new_board, goal)
            neighbors.append(PuzzleState(new_board, state, (new_x, new_y), g, heuristic))
    return neighbors

def a_star_search(start, goal, heuristic_func):
    boardQueue = PriorityQueue()
    start_state = PuzzleState(start, g=0, heuristic=heuristic_func(start, goal))
    boardQueue.put(start_state)
    boardVisited = set()

    steps = 0  # Counter for the number of steps (nodes expanded)

    while not boardQueue.empty():
        current_state = boardQueue.get()
        steps += 1  # Increment step counter for each expanded node

        if current_state.board == goal:
            return reconstruct_path(current_state), steps, current_state.g  # Return the solution path, steps, and cost

        boardVisited.add(current_state)

        for neighbor in generate_neighbors(current_state, goal, heuristic_func):
            if neighbor not in boardVisited and all(not (node == neighbor and node.f() <= neighbor.f()) for node in boardQueue.queue):
                boardQueue.put(neighbor)

    return None, steps, None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

# Example usage
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

path_manhattan, steps_manhattan, cost_manhattan = a_star_search(start, goal, manhattan_distance)
print("Manhattan Distance Heuristic:")
if path_manhattan:
    for step in path_manhattan:
        for row in step:
            print(row)
        print()

else:
    print("No solution found.")
print()

path_misplaced, steps_misplaced, cost_misplaced = a_star_search(start, goal, misplaced_tiles)
print("Misplaced Tiles Heuristic:")
if path_misplaced:
    for step in path_misplaced:
        for row in step:
            print(row)
        print()
    print(f"misplaced steps: {steps_misplaced}")
    print(f"Cost of path misplaced: {cost_misplaced}")
else:
    print("No solution found.")

print(f"manhattan steps: {steps_manhattan}")
print(f"Cost of path manhattan: {cost_manhattan}")