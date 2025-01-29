def dfs_iterative(adj, start):
    stack = [start] 
    visited = [False] * len(adj)  
    
    while stack:
        node = stack.pop()  
        if not visited[node]:
            print(node, end=" ")  
            visited[node] = True 
            
            for neighbor in reversed(adj[node]): 
                if not visited[neighbor]:
                    stack.append(neighbor)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    V = int(input("Enter number of nodes: "))
    adj = [[] for _ in range(V)] 

    print("Enter the edges (-1, -1 to exit):")
    while True:
        i = int(input("i = "))
        j = int(input("j = "))
        if i == -1 and j == -1: 
            break
        add_edge(adj, i, j)

    start_node = int(input("Enter the starting node for DFS: "))
    print(f"DFS starting from {start_node}:")
    dfs_iterative(adj, start_node)
