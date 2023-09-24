N, M, I = map(int, input().strip().split())
ages = []
graph = {i: [] for i in range(1, N + 1)}
ages = [int(x) for x in input().strip().split()]
for _ in range(M):
    X, Y = map(int, input().strip().split())
    graph[X].append(Y)
#####################

visited = []
numbers = []

def reverse(adj):
    rev = {node: [] for node in adj}
    for node in adj.keys():
        for neigh in adj[node]: rev[neigh].append(node)
    return rev

def dfs_lowest(adj, node):
    rev = reverse(adj)
    if not rev[node]: return "*"
    dfs_visit(rev, node)
    numbers.pop(0)
    return min(numbers)

def dfs_visit(adj, node):
    visited.append(node)
    numbers.append(ages[node - 1])
    for neigh in adj[node]:
        if not neigh in visited:
            dfs_visit(adj, neigh)

while True:
    try:
        x = input().strip().split()
        if len(x) == 2:
            print(dfs_lowest(graph, int(x[1])))
            numbers.clear()
            visited.clear()
        elif len(x) == 3:
            a, b = int(x[1]), int(x[2]) 
            graph[a], graph[b] = graph[b], graph[a]
            for node in graph.keys():
                if a in graph[node]:
                    graph[node].remove(a)
                    graph[node].append(b)
                elif b in graph[node]:
                    graph[node].remove(b)
                    graph[node].append(a)
    except EOFError:
        break