import queue as Q

def Astar(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((int(graph[start]['heuristic']), [start])) #{(hu(b)+w(s,a)+w(a,b),[s a b])}
    visited=[]                                           #{(hu(d)+w(s,a)+w(a,b)+w(b,d),[s a b d])}
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            print("Path found: " + str(node[1]))
            break
    #Node A=h(A)+path(S,A)=40   neigh=C   Que.put( cost (H(C)+pathcost (S,C)),path [S,A, C] ) 
        for neighbor in graph[current]['neighbors']: #current =A  neigh=[(C,1)]
            temp = node[1][:]
            temp.append(neighbor[0])
            # scost=node[0]-graph[current]["heuristic"]+neighbor[1]+graph[neighbor[0]]['heuristic']
            cost=int(graph[neighbor[0]]['heuristic'])+(node[0]- int( graph[current]['heuristic']))+neighbor[1]
            queue.put((cost, temp))
        
def readGraph():
    lines = int( input() )
    graph = {}
    
    for line in range(lines):
        line = input()
            
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}
        graph[node]['heuristic'] = tokens[1] # it is expected value for reach to the goal
        graph[node]['neighbors']=[] 
        for i in range(2,len(tokens)-1 , 2):
            graph[node]['neighbors'].append((tokens[i],int(tokens[i + 1])))
    return graph

def main():
    graph = readGraph()
    Astar(graph, 'S', 'G')
    
if __name__ == "_main_":
    main()

#####SAMPLE INUPT A*
# 6
# S 5 A 1 G 10
# A 3 B 2 C 1
# B 4 D 5
# C 2 D 3 G 4
# D 6 G 2
# G 0