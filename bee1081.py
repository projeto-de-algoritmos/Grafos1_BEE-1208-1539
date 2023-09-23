visited = []
def pathR(adj: dict):
    for node in sorted(adj.keys()):
        if not node in visited:
            dfs_visit(adj, node, 1)
            if adj[node]: print("")

def dfs_visit(adj, node, tabs):
    visited.append(node)
    for neigh in sorted(adj[node]):
        spacing = "  " * tabs
        if not neigh in visited:
            print(f"{spacing}{node}-{neigh} pathR(G,{neigh})")
            dfs_visit(adj, neigh, tabs + 1)
        else: print(f"{spacing}{node}-{neigh}")

N = int(input())
for i in range(N):
    v, e = map(int, input().strip().split())
    graph = {x: [] for x in range(v)}
    for _ in range(e):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
    print(f"Caso {i+1}:")
    pathR(graph)
    graph.clear(), visited.clear()
