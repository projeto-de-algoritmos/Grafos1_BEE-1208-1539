def gR(graph):
    rev = {node: [] for node in graph}
    for node in graph:
        for neigh in graph[node]:
            rev[neigh].append(node)
    return rev


visited = []
def dfs(graph):
    count = 0
    for node in graph:
        if count > 1: return len(visited)
        count += 1
        if not node in visited:
            dfs_visit(graph, node)

def dfs_visit(graph, node):
    visited.append(node)
    # print(visited, graph)
    print("node = ", node, graph)
    for neigh in graph[node]:
        if not neigh in visited:
            dfs_visit(graph, neigh)

N, M = map(int, input().strip().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    U, V = map(int, input().strip().split())
    graph[U].append(V)

if dfs(graph) == N: print("1Bolada")
elif dfs(gR(graph)) == N: print("2Bolada")
else: print("Nao Bolada")