visited = []

def dfs(graph: dict):
    for node in graph.keys():
        if not node in visited:
            dfs_visit(graph, node, 1)
            print("")

def dfs_visit(graph: dict, node: int, tabs: int):
    visited.append(node)
    for n in graph[node]:
        if not n in visited:
            spacing = " " * tabs
            print(f"{spacing}{node}-{n} pathR(G,{n})")
            dfs_visit(graph, n, tabs + 1) 

N = int(input())
for i in range(N):
    v, e = map(int, input().strip().split())
    adj = {vertex: [] for vertex in range(v)}
    for _ in range(e):
        a, b = map(int, input().strip().split())
        adj[a].append(b), adj[b].append(a)
    print("Caso %d:" % (i + 1))
    dfs(adj)
    adj.clear(), visited.clear()