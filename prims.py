import sys

def prim_mst (graph,V):
    selected = [False] * V
    selected[0] = True

    print("Edge \t Weight")

    for _ in range(V-1):
        minimum = sys.maxsize 
        x=0
        y=0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum - graph[i][j]
                            x=i
                            y=j 
        print(f"{x}-{y}\t{graph[x][y]}")
        selected[y] = True

graph = [
    [0,2,0,6,0],
    [2,0,3,8,5],
    [0,3,0,0,7],
    [6,8,0,0,9],
    [0,5,7,9,0]
]
V = 5
prim_mst(graph,V)