# Check if it's safe to assign a color to a vertex
def is_safe(vertex, color, assignment, graph):
    for neighbor in graph[vertex]:
        if assignment[neighbor] == color:
            return False
    return True

# Recursive function to solve the coloring problem
def graph_coloring(graph, m, assignment, vertex=0):
    if vertex == len(graph):
        return True  # All vertices are colored

    for color in range(1, m + 1):
        if is_safe(vertex, color, assignment, graph):
            assignment[vertex] = color
            if graph_coloring(graph, m, assignment, vertex + 1):
                return True
            assignment[vertex] = 0  # Backtrack

    return False

# ---- Main Program ----
def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    # Initialize graph
    graph = [[] for _ in range(n)]
    print("Enter edges (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    m = int(input("Enter number of colors: "))
    assignment = [0] * n

    if graph_coloring(graph, m, assignment):
        print("Coloring of graph:")
        for i, c in enumerate(assignment):
            print(f"Vertex {i}: Color {c}")
    else:
        print(f"No valid coloring possible with {m} colors.")

if __name__ == "__main__":
    main()
