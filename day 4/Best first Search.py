# import queue as Q

# def BESTFS(graph, start, end):
#     if start not in graph:
#         raise TypeError(str(start) + ' not found in graph !')
#         return
#     if end not in graph:
#         raise TypeError(str(end) + ' not found in graph !')
#         return
    
#     queue = Q.PriorityQueue()
#     queue.put((graph[start]['heuristic'], [start])) #q={(3,[S B]),} 
#     while not queue.empty():
#         node = queue.get() #node =  (2, [S A])
#         current = node[1][-1] #current= A
#         if end in node[1]:
#             print("Path found: " + str(node[1]))
#             break
        
#         for neighbor in graph[current]['neighbors']: #neigh=[>>C D ]
#             temp = node[1][:] # [S A]
#             temp.append(neighbor) #temp=[S A]
#             queue.put((graph[neighbor]['heuristic'], temp)) # (1, [S A C])
        
# def readGraph():
#     lines = int( input() )
#     graph = {}
    
#     for line in range(lines):
#         line = input()
            
#         tokens = line.split()
#         node = tokens[0]
#         graph[node] = {}
#         graph[node]['heuristic'] = tokens[1]
#         graph[node]['neighbors'] = tokens[2:]
#     return graph

# def main():
#     graph = readGraph()
#     BESTFS(graph, 'S', 'G')
    
# if _name_ == "_main_":
#     main()

# #####SAMPLE INUPT Best First Search
# # 6
# # S 10 B A
# # A 2 C D
# # B 3 D G
# # C 1
# # D 4 C G
# # G 0

# --------------
from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
    
    def __lt__(self, other):#<
        return self.heuristic < other.heuristic

def greedy_best_first_search(start, goal, heuristic_func, neighbors_func):
    open_list = PriorityQueue()
    open_list.put(Node(start, heuristic=heuristic_func[start])) #(s,10)
    closed_list = set()
    
    while not open_list.empty():
        current_node = open_list.get() #instance of node
        current_state = current_node.state #string (S) node.state
        
        if current_state == goal:
            return reconstruct_path(current_node)
        
        closed_list.add(current_state)
        
        for neighbor in neighbors_func[current_state]:
            if neighbor in closed_list:
                continue
            new_node = Node(neighbor, current_node, heuristic=heuristic_func[neighbor])
            open_list.put(new_node)
    
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)  #[G A S]
        node = node.parent
    path.reverse() #return path[::-1]
    return path 

heuristic_func = {
    'S': 10,
    'A': 2,
    'B': 3,
    'C': 1,
    'D': 4,
    'G': 0
}

neighbors_func = {
    'S': ['B', 'A'],
    'A': ['C', 'D'],
    'B': ['D', 'G'],
    'C': [],
    'D': ['C', 'G'],
    'G': []
}

start = 'S'
goal = 'G'
path = greedy_best_first_search(start, goal, heuristic_func, neighbors_func)

print("Path found:", path)