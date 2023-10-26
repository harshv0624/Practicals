def aStarAlgo(start_node, stop_node, closed_set=None):

    open_set = set(start_node)
    close_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] - g[n] + weight
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == stop_node:
            path =[]
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

        open_set.remove(n)
        close_set.add(n)
    print('path found: {}'.format(path))
    return path
def get_neighbours(v):
    if v in Graph_nodes:
        return Graph_nodes(v)
    else:
        return None

def heuristic(n):
    H_dist = {
    'A': 22,
    'B': 30,
    'C': 1,
    'D': 11,
    'E': 25,
    'G': 0,
    }
    return H_dist[n]
Graph_nodes = {
    'A': [('B',2),('E',5)],
    'B': [('C',9),('G',4)],
    'C': None,
    'D': [('G',1)],
    'E': [('D',7),],
}
aStarAlgo(start_node:'A',stop_node:'G'):
