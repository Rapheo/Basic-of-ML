import sys
def create_graph():
    
    global graph
    global participents
    with open("input_3.txt", "r") as input_file:
        file_contain = input_file.read().splitlines()
        total_nodes = int(file_contain.pop(0))
        total_edges = int(file_contain.pop(0))

        temp_graph = []
        for i in range (total_edges):
            temp_graph.append(file_contain.pop(0))
        
        graph = {}
        for i in range(len(temp_graph)):
            for j in temp_graph:
                if(int(j[0]) == i):
                    graph.setdefault(int(j[2]), []).append(
                        int(j[0]))  # reversing directed graph edges  

        start_pos = int(file_contain.pop(0))
        number_of_participants = int(file_contain.pop(0))
        participents = []
        for i in range(number_of_participants):
            participents.append(int(file_contain.pop(0)))
        return(bfs(start_pos))
        


visited = [] #List to keep track of visited nodes.
queue = []   #Initialize a queue


def bfs(node):
    parent = {}
    visited.append(node)
    queue.append(node)
    x = []
    while queue:
        s = queue.pop(0)
        x.append(s)
        value = x[len(x)-1]
        if value in participents:           #finding every participents parents in one search
            concatinate = []
            temp = value
            for i in reversed(x):
                if(value != i and i != 0 and temp in graph[i]):
                    concatinate.append(i)
                    temp = i
            parent.setdefault(value, []).append(concatinate)       

        if s == 0:
            break
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return parent               

# Driver Code
parent = create_graph()
minz = sys.maxsize
result = -1
for k, v in parent.items():
    if(len(v[0]) < minz):
        minz = len(v[0])
        result = k

print(minz)