from collections import defaultdict

# Graph class
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge to the undirected graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive DFS function
    def dfs_recursive(self, vertex, visited):
        print(vertex, end=' ')
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Wrapper for DFS
    def dfs(self, start_vertex):
        visited = set()
        print("DFS Traversal:")
        self.dfs_recursive(start_vertex, visited)

# --- Main Program ---

g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("Enter starting vertex: ")
g.dfs(start)
