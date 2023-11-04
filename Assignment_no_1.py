graph = {
    "0": ["3", "1"],
    "3": ["0", "1", "2","4"],
    "1": ["0", "3", "2","5","6"],
    "2": ["3","1","4","5"],
    "4": ["3","2","6"],
    "5": ["2","1"],
    "6": ["4","1"]
}


def bfs( start):
    visited = []
    queue = [start]
    while queue:
        print(queue)
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            neighbors = graph[v]
            for neighbors in neighbors:
                queue.append(neighbors)

    print(visited)


# num_of_nodes = int(input("Enter Number Of Nodes:"))
# for i in range(num_of_nodes):
#     name_of_node = input("Enter Node letter: ")
#     neighbors = input("Enter Neighbors: ").split(" ")
#     graph[name_of_node] = [neighbors.strip() for neighbors in neighbors]

bfs("0")
