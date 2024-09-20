import numpy as np
import random

GRID_SIZE = 3
OBSTACLE = (1, 1)
GOAL = (2, 2)
START = (0, 0)

ACTIONS = ['up', 'down', 'left', 'right']
action_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

q_table = np.zeros((GRID_SIZE, GRID_SIZE, len(ACTIONS)))

alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_decay = 0.99
min_epsilon = 0.1
episodes = 500

reward_goal = 10
penalty_step = -1

def is_valid_position(state):
    x, y = state
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and state != OBSTACLE

# Choose action based on epsilon-greedy policy
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(ACTIONS)
    else:
        # Exploit: choose the action with the highest Q-value
        x, y = state
        return ACTIONS[np.argmax(q_table[x, y])]

def take_action(state, action):
    x, y = state
    move = action_dict[action]
    new_state = (x + move[0], y + move[1])

    # Check if new state is valid
    if not is_valid_position(new_state):
        return state, penalty_step  # Invalid move, stay in the same state and penalize

    if new_state == GOAL:
        return new_state, reward_goal  # Goal reached

    return new_state, penalty_step  # Normal step with penalty

# Q-learning algorithm
for episode in range(episodes):
    state = START
    done = False

    while not done:
        action = choose_action(state)

        new_state, reward = take_action(state, action)

        # Q-learning update
        x, y = state
        nx, ny = new_state
        action_index = ACTIONS.index(action)

        # Update Q-value
        q_table[x, y, action_index] += alpha * (reward + gamma * np.max(q_table[nx, ny]) - q_table[x, y, action_index])

        state = new_state

        if state == GOAL:
            done = True

    # Decay epsilon to reduce exploration over time
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    # Print progress every 50 episodes
    if episode % 50 == 0:
        print(f"Episode {episode}: Epsilon = {epsilon}")

# # Final Q-table
print("\nFinal Q-Table:")
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if (i, j) == OBSTACLE:
            print(f"({i},{j})", "Obstacle")
        else:
            print(f"({i},{j})", q_table[i, j])