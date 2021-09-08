def create_graph():

    global graph
    with open("input.txt", "r") as input_file:

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
                    graph.setdefault(
                        int(j[0]), []).append(int(j[2]))
                    graph.setdefault(int(j[2]), []).append(
                        int(j[0]))  # undirected edges connects both ways   
        goal_pos =  int(file_contain.pop(0))
        start_pos = 0                       
        steps = bfs(start_pos, goal_pos)
        print(len(steps)-1)   # -1 for calculating the steps from the total nodes


def bfs(start_pos, goal_pos):
    if(start_pos == goal_pos):
        return goal_pos
    

    visited = []
    queue = []

    queue.append([start_pos])

    while queue:
        forward = queue.pop(0)
        backward = forward[-1]

        if backward not in visited:
            near = graph[backward]

            for n in near:
                traverse = list(forward)
                traverse.append(n)
                queue.append(traverse)

                if n == goal_pos:
                    return traverse
            visited.append(backward)

# Driver Code
create_graph()

