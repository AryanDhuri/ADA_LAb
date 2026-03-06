import sys

# Helper functions for Union-Find to detect cycles
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(graph, V):
    edges = []
    # 1. Extract all edges from the adjacency matrix
    for i in range(V):
        for j in range(i + 1, V): # Avoid duplicates (i-j and j-i)
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # 2. Sort edges by weight (the greedy step)
    edges.sort(key=lambda item: item[2])

    parent = list(range(V))
    rank = [0] * V
    mst_edges = 0
    i = 0

    print("Edge \t Weight")

    # 3. Iterate through sorted edges
    while mst_edges < V - 1 and i < len(edges):
        u, v, w = edges[i]
        i += 1
        
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If adding the edge doesn't cause a cycle
        if root_u != root_v:
            mst_edges += 1
            print(f"{u}-{v}\t{w}")
            union(parent, rank, root_u, root_v)

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
V = 5
kruskal_mst(graph, V)
