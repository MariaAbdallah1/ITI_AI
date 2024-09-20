from pickle import TRUE
import queue

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = None
        # whether the node was reached by the BFS that started from source
        self.visited_right = False
        # whether the node was reached by the BFS that started from destination
        self.visited_left = False
        # used for retrieving the final path from start to the meeting point
        self.parent_right = None
        # used for retrieving the final path from the meeting point to destination
        self.parent_left = None


def extract_path(node): #node=6
    """return the path when both BFS's have met"""
    node_copy = node
    path = []

    while node:
        path.append(node.val) # 6 1 0
        node = node.parent_right
    path.reverse() # 0 1 
    del path[-1]  # because the meeting node appears twice

    while node_copy:
        path.append(node_copy.val)  #0 1 6 3 4
        node_copy = node_copy.parent_left
    return path


def bidirectional_search(s, t):
    
    q = queue.Queue() 
    q.put(s)
    q.put(t) 
    s.visited_right = True #forward
    t.visited_left = True #backward
    while not q.empty(): ##q=]  6 6]
        n = q.get() #n= 6
        if n.visited_left and n.visited_right:  # if the node visited by both BFS's
            return extract_path(n)
        for neigbor in n.neighbors:  #nes [1]
            if n.visited_left == True and not neigbor.visited_left:
                neigbor.parent_left = n
                neigbor.visited_left = True
                q.put(neigbor)
            if n.visited_right == True and not neigbor.visited_right:
                neigbor.parent_right = n
                neigbor.visited_right = True
                q.put(neigbor)

    return False


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n0.neighbors = [n1, n5]
n1.neighbors = [n0, n2, n6]
n2.neighbors = [n1]
n3.neighbors = [n4, n6]
n4.neighbors = [n3]
n5.neighbors = [n0, n6]
n6.neighbors = [n1, n3, n5, n7]
n7.neighbors = [n6]
print(bidirectional_search(n0, n4))