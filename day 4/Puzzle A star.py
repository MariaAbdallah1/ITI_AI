from queue import PriorityQueue

class PuzzleState:
    def __init__(self, board, parent=None, move=None, g=0, heuristic=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  # Cost to reach the current node
        self.heuristic = heuristic  # Estimated cost to reach the goal (h)

    def f(self):
        return self.g + self.heuristic  # Total cost function f = g + h

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
                goal_x, goal_y = divmod(goal_flat.index(board[i][j]), 3)  #(a // b, a % b)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def generate_neighbors(state, goal):
    neighbors = []
    empty_x, empty_y = state.find_empty()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in state.board]
            new_board[empty_x][empty_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[empty_x][empty_y]
            g = state.g + 1  # Cost to reach the neighbor
            heuristic = manhattan_distance(new_board, goal)
            neighbors.append(PuzzleState(new_board, state, (new_x, new_y), g, heuristic))
    return neighbors

def a_star_search(start, goal):
    boardQueue = PriorityQueue()
    start_state = PuzzleState(start, g=0, heuristic=manhattan_distance(start, goal))
    boardQueue.put(start_state)
    boardVisited = set()

    while not boardQueue.empty():
        current_state = boardQueue.get()

        if current_state.board == goal:
            return reconstruct_path(current_state)

        boardVisited.add(current_state)

        for neighbor in generate_neighbors(current_state, goal):
            if neighbor not in boardVisited and all(not (node == neighbor and node.f() <= neighbor.f()) for node in boardQueue.queue):
                boardQueue.put(neighbor)

    return None

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

path = a_star_search(start, goal)
if path:
    for step in path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")