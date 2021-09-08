from queue import Queue
import numpy as np

visited=[]  

def initialization(x,directed):
    file = x
  
    global vertexCount
    vertexCount = int(file.readline().strip())
    
    edgeCount = int(file.readline().strip())
    
    global adjMatrix
    adjMatrix = np.zeros((vertexCount,vertexCount),dtype='int')
    
    for i in range(edgeCount):
        line = file.readline().strip()
                
        vertices = line.split(' ')
        u = int(vertices[0])
        v = int(vertices[1])
        adjMatrix[u][v] +=1
        if(directed):
            adjMatrix[v][u] +=1
          
    global color
    color = np.empty((vertexCount),dtype= 'object') 
    color[:]='white'
    global parent
    parent = np.empty((vertexCount),dtype= 'object') 
    parent[:]= np.NaN
    global distance
    distance = np.empty((vertexCount),dtype= 'object')  
    distance[:] =99999
    
    global myQueue
    myQueue = Queue(maxsize = vertexCount)
    
def bfs(s):
    color[s]= 'gray'
    parent[s]= np.nan
    distance[s]=0
    myQueue.put(s)
    while not myQueue.empty():
        u = myQueue.get()
        for v in range(vertexCount):
            if adjMatrix[u][v]==1:
                if color[v]== 'white':
                    color[v]= 'gray'
                   
                    distance[v]=distance[u]+1
                    parent[v]=u
                    
                    myQueue.put(v)
        color[u]= 'black'
        print(u, 'to ',str(s),' distance: ',distance[u]) 
        
    return distance       
 
# Dfs recursion code for tree structure 
def dfs(s,visited,adjMatrix,vertexCount):
    if s not in visited:
        visited.append(s)   
        u=s 
        for v in range(vertexCount):
            if adjMatrix[u][v]==1:
                
                if v not in visited:
                    distance[v]=distance[u]+1
               
                dfs(v)
                    
        print(u, ' distance: ',distance[u])  

'''
level 1 outputs, here initialization sets up the value for the input file
True is for undirected graph 
'''
print('level 1 outputs')
file=open('input1.txt','r')      
initialization(file,True)
LinasPosition = int(file.readline().strip())

distance=bfs(LinasPosition)
NorasPosition=0
print()
print("Minimum number of moves Nora needs to go to ‘x’ Lina's Positon")
print(distance[NorasPosition]) 

print('')


'''
level 2 outputs, here initialization sets up the value for the input file
True is for undirected graph 
'''
print('level 2 outputs')
file=open('input2.txt','r')      
initialization(file,True)
LinasPosition = int(file.readline().strip())
distance=bfs(LinasPosition)

NorasPosition=int(file.readline().strip())
NoraDistance=distance[NorasPosition]

LarasPosition=int(file.readline().strip())
LaraDistance=distance[LarasPosition]

print()
if LaraDistance<NoraDistance:
    print("Lara     is the winner, distance ",LaraDistance)
else:
    print("Nora     is the winner, distance ",NoraDistance)
print('')


'''
level 3 outputs, here initialization sets up the value for the input file
False is for directed graph 
'''
print('level 3 outputs')
file=open('input3.txt','r')      
initialization(file,False)
LinasPosition = int(file.readline().strip())
# distance=bfs()  # print(distance[LinasPosition])

lista =[]
listb =[]
totalParticipants =int(file.readline().strip())

for i in range(totalParticipants):
    k=int(file.readline().strip())
    lista.append(k)
    
for i in lista:
    file=open('input3.txt','r')  
    initialization(file,False)
    distance=bfs(i)
    listb.append(distance[LinasPosition])
    
# print(lista)   # print(listb)   
position=0
minMoves=9999
for i in range(totalParticipants):
    if listb[i]<=minMoves:
        minMoves=listb[i]
        position=i+1
        
print()
print(minMoves,'   minimum number of moves for participant ',position,' to win')