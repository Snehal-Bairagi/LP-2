from collections import defaultdict, deque

# Create a graph class
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge to undirected graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Recursive BFS using a helper function
    def bfs_recursive(self, queue, visited):
        if not queue:
            return

        current = queue.popleft()
        print(current, end=' ')
        
        for neighbor in self.graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        
        self.bfs_recursive(queue, visited)

    # Driver function
    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        print("BFS Traversal:")
        self.bfs_recursive(queue, visited)

# ---- Main Program ----

g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("Enter starting vertex: ")
g.bfs(start)
