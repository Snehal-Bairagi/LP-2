import heapq
from collections import defaultdict

def prims_mst(n, edges):
    graph = defaultdict(list)

    # Build the undirected weighted graph
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = set()
    mst_weight = 0
    mst_edges = []

    # Min-heap to pick minimum weight edge
    min_heap = [(0, 0, 0)]  # (weight, from_node, to_node), start from node 0

    while min_heap and len(visited) < n:
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue
        visited.add(v)
        mst_weight += weight
        if u != v:
            mst_edges.append((u, v, weight))
        for next_weight, neighbor in graph[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (next_weight, v, neighbor))

    return mst_weight, mst_edges

# ---- Main program ----

# Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v w):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst_weight, mst_edges = prims_mst(n, edges)

print("\nMinimum Spanning Tree edges:")
for u, v, w in mst_edges:
    print(f"{u} - {v} (weight {w})")

print(f"\nTotal weight of MST: {mst_weight}")
