graph = {
    "0": ["3", "1"],
    "3": ["0", "1", "2", "4"],
    "1": ["0", "3", "2", "5", "6"],
    "2": ["3", "1", "4", "5"],
    "4": ["3", "2", "6"],
    "5": ["2", "1"],
    "6": ["4", "1"],
}

def dfs(graph,start,visited=None):
    if visited==None:
        visited=set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

dfs(graph,'2')

