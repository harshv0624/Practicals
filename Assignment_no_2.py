


import heapq

grid = [
    ['S', ' ', ' ', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', ' ', 'X', 'X'],
    [' ', ' ', ' ', ' ', ' ', ' '],
    ['X', 'X', 'X', 'X', 'X', 'G']
]

def heurisitic(node):
    x1, y1 = node
    x2, y2 = goal
    ans= abs(x1 - x2) + abs(y1 - y2)
    return ans


start = (0, 0)
open_list = []
goal = (5, 5)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

costs = {}
parents = {}

heapq.heappush(open_list, (0, start))

found_goal = False

while open_list:
    cost, current = heapq.heappop(open_list)
    if current == goal:
        found_goal = True
        break

    for move in moves:
        x, y = current[0] + move[0], current[1] + move[1]

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "X":
            new_cost = cost + 1
            if (x, y) not in costs or new_cost < costs[(x, y)]:
                costs[(x, y)] = new_cost
                priority = new_cost + heurisitic((x, y))
                heapq.heappush(open_list, (priority, (x, y)))
                parents[(x, y)] = current

if found_goal:
    print("Goal Reached")
    path = []
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()
    print(path)
else:
    print("No path to the goal.")



def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, goal):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])

    open_list = [(0, start)]
    costs = {start: 0}
    parents = {}

    while open_list:
        open_list.sort()  # Sort by cost (you can replace this with your own sorting)
        cost, current = open_list.pop(0)

        if current == goal:
            found_goal = True
            break

        for move in moves:
            x, y = current[0] + move[0], current[1] + move[1]

            if 0 <= x < rows and 0 <= y < cols and grid[x][y] != "X":
                new_cost = costs[current] + 1

                if (x, y) not in costs or new_cost < costs[(x, y)]:
                    costs[(x, y)] = new_cost
                    priority = new_cost + heuristic((x, y), goal)
                    open_list.append((priority, (x, y)))
                    parents[(x, y)] = current

    if found_goal:
        print("Goal Reached")
        path = []
        while current != start:
            path.append(current)
            current = parents[current]
        path.append(start)
        path.reverse()
        print(path)
    else:
        print("No path to the goal")

# Define your grid
grid = [
    ['S', ' ', ' ', ' ', ' ', ' '],
    [' ', 'X', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', ' ', 'X', 'X'],
    [' ', ' ', ' ', ' ', ' ', ' '],
    ['X', 'X', 'X', 'X', 'X', 'G']
]

start = (0, 0)
goal = (5, 5)
astar(grid, start, goal)

