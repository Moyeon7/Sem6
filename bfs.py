from collections import deque

def bfs(adj, s):
    q = deque()
    visited = [False] * len(adj)  
    visited[s] = True
    parent = [None] * len(adj)            
    q.append(s)                 
    
    while q:
        curr = q.popleft()
        print(curr, end=" ")     

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x) 
                parent[x] = curr  
    
    print("Path: ")
    for k in range(len(parent)):
        path = []
        c=k
        while k is not None:
            path.append(k)
            k = parent[k]
        print(f"Path to {c}: {' -> '.join(map(str, reversed(path)))}")



def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

V = int(input("Enter number of nodes: "))
adj = [[] for _ in range(V)] 

print("Enter the edges (-1, -1 to exit):")
while True:
    i = int(input("i = "))
    j = int(input("j = "))
    if i == -1 and j == -1:  
        break
    add_edge(adj, i, j)

start_node = int(input("Enter the starting node for BFS: "))
print(f"BFS starting from {start_node}:")
bfs(adj, start_node)
