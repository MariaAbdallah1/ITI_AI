import pandas as pd
from queue import PriorityQueue
import queue as Q

class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return self.heuristic < other.heuristic

def greedy_best_first_search(start, goal, heuristic_func, neighbors_func):
    open_list = PriorityQueue()
    open_list.put(Node(start, heuristic=heuristic_func[start]))
    closed_list = set()
    
    while not open_list.empty():
        current_node = open_list.get()
        current_state = current_node.state
        
        if current_state == goal:
            return reconstruct_path(current_node)
        
        closed_list.add(current_state)
        
        for neighbor, _ in neighbors_func.get(current_state, []):
            if neighbor in closed_list:
                continue
            new_node = Node(neighbor, current_node, heuristic=heuristic_func.get(neighbor, 0))
            open_list.put(new_node)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path

def a_star_search(graph, start, goal):
    if start not in graph:
        raise TypeError(f'{start} not found in graph!')
    if goal not in graph:
        raise TypeError(f'{goal} not found in graph!')
    
    queue = Q.PriorityQueue()
    queue.put((graph[start]['heuristic'], [start]))
    visited = set()
    
    while not queue.empty():
        cost, path = queue.get()
        current = path[-1]
        
        if current == goal:
            return path
        
        visited.add(current)
        
        for neighbor, weight in graph.get(current, {}).get('neighbors', []):
            if neighbor in visited:
                continue
            new_path = path + [neighbor]
            new_cost = cost + weight + graph.get(neighbor, {}).get('heuristic', 0) - graph.get(current, {}).get('heuristic', 0)
            queue.put((new_cost, new_path))
    
    return None

def load_data(filename, key_col, value_col):
    df = pd.read_csv(filename)
    return dict(zip(df[key_col], df[value_col]))

def load_actor_movie_relationships(filename):
    actor_movie_map = {}
    movie_actor_map = {}
    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        actor_id, movie_id = int(row['person_id']), int(row['movie_id'])
        actor_movie_map.setdefault(actor_id, set()).add(movie_id)
        movie_actor_map.setdefault(movie_id, set()).add(actor_id)
    return actor_movie_map, movie_actor_map

def build_actor_graph(actor_movie_map, movie_actor_map):
    graph = {}
    for movie, actors in movie_actor_map.items():
        actors_list = list(actors)
        for i in range(len(actors_list)):
            for j in range(i + 1, len(actors_list)):
                graph.setdefault(actors_list[i], {'heuristic': 0, 'neighbors': []})
                graph.setdefault(actors_list[j], {'heuristic': 0, 'neighbors': []})
                graph[actors_list[i]]['neighbors'].append((actors_list[j], 1))
                graph[actors_list[j]]['neighbors'].append((actors_list[i], 1))
    return graph

def main():
    actor_file = 'C:/Users/Maria Abdallah/Downloads/Maria_iti/day 3/people.csv'
    movie_file = 'C:/Users/Maria Abdallah/Downloads/Maria_iti/day 3/movies.csv'
    relationship_file = 'C:/Users/Maria Abdallah/Downloads/Maria_iti/day 3/stars.csv'

    actors = load_data(actor_file, 'id', 'name')
    movies = load_data(movie_file, 'id', 'title')
    actor_movie_map, movie_actor_map = load_actor_movie_relationships(relationship_file)
    
    actor_graph = build_actor_graph(actor_movie_map, movie_actor_map)
    
    # Calculate heuristics (Manhattan distance as example, though not really applicable for actors)
    for actor in actor_graph:
        actor_graph[actor]['heuristic'] = abs(actor - 102)  # Simple heuristic example
    
    kevin_bacon_id = 102
    print("Available actors:")
    for actor_id, actor_name in actors.items():
        print(f"{actor_id}: {actor_name}")
    
    try:
        example_actor_id = int(input("\nEnter the ID of the other actor: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return
    
    if example_actor_id not in actors:
        print("Actor ID not found.")
        return
    
    # GBFS Path
    gbfs_path = greedy_best_first_search(example_actor_id, kevin_bacon_id, 
                                         lambda x: actor_graph.get(x, {}).get('heuristic', 0),
                                         actor_graph)
    
    # A* Path
    astar_path = a_star_search(actor_graph, example_actor_id, kevin_bacon_id)
    
    def format_path(path):
        if path is None:
            return "No path found"
        return [(actors[id1], actors[id2], movies[movie]) for id1, id2, movie in path]

    print("\nGreedy Best-First Search Path:")
    if gbfs_path:
        print(" -> ".join(str(actors[actor_id]) for actor_id in gbfs_path))
    else:
        print("No path found")

    print("\nA* Search Path:")
    if astar_path:
        print(" -> ".join(str(actors[actor_id]) for actor_id in astar_path))
    else:
        print("No path found")

if __name__ == "__main__":
    main()
