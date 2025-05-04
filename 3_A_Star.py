import heapq

# Print the board in 3x3 format
def print_board(state):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if state[i] == -1 else state[i], end=" ")
    print("\n")

# Check if the puzzle is solvable
def solvable(start):
    inv = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if start[i] != -1 and start[j] != -1 and start[i] > start[j]:
                inv += 1
    return inv % 2 == 0

# Heuristic: Manhattan Distance
def manhattan(start, goal):
    h = 0
    for i in range(9):
        if start[i] == -1:
            continue
        idx_goal = goal.index(start[i])
        h += abs(i // 3 - idx_goal // 3) + abs(i % 3 - idx_goal % 3)
    return h

# Generate neighbors of a given state
def get_neighbors(state):
    neighbors = []
    pos = state.index(-1)
    row, col = pos // 3, pos % 3

    def swap_and_clone(i, j):
        new_state = state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    if row > 0:  # Up
        neighbors.append(swap_and_clone(pos, pos - 3))
    if row < 2:  # Down
        neighbors.append(swap_and_clone(pos, pos + 3))
    if col > 0:  # Left
        neighbors.append(swap_and_clone(pos, pos - 1))
    if col < 2:  # Right
        neighbors.append(swap_and_clone(pos, pos + 1))

    return neighbors

# A* Search Algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan(start, goal), 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        state_tuple = tuple(current)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current == goal:
            print("Solution found in", g, "moves.\n")
            for p in path:
                print_board(p)
            return

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                h = manhattan(neighbor, goal)
                heapq.heappush(open_list, (g + 1 + h, g + 1, neighbor, path + [neighbor]))

    print("No solution found.")

# Main function
def main():
    print("Enter the start state (use -1 for empty):")
    start = [int(input()) for _ in range(9)]

    print("Enter the goal state (use -1 for empty):")
    goal = [int(input()) for _ in range(9)]

    print("\nStart State:")
    print_board(start)

    print("Goal State:")
    print_board(goal)

    if solvable(start):
        a_star(start, goal)
    else:
        print("This puzzle is not solvable.")

if __name__ == "__main__":
    main()

"""
📌 Example Input:
Start: [1, 2, 3, 4, -1, 6, 7, 5, 8]
Goal:  [1, 2, 3, 4, 5, 6, 7, 8, -1]

✅ Output:
Solution found in 2 moves.

Start State:
1 2 3
4 _ 6
7 5 8

Goal State:
1 2 3
4 5 6
7 8 _

Steps:
1 2 3
4 _ 6
7 5 8

1 2 3
4 5 6
7 _ 8

1 2 3
4 5 6
7 8 _

"""
