visited = []
numbers = []

def g_reverse(graph): # O(n + m)
    rev = {node: [] for node in graph}
    for node in graph.keys():
        for item in graph[node]:
            rev[item].append(node)
    return rev

def dfs_visit(graph, node, ages):
    visited.append(node)
    numbers.append(ages[node - 1])
    for neigh in graph[node]:
        if not neigh in visited:
            dfs_visit(graph, neigh, ages)    

def fewest(graph, node, ages):
    reverse = g_reverse(graph)
    if not reverse[node]: return "*"
    dfs_visit(reverse, node, ages)
    numbers.pop(0)
    minimum = min(numbers)
    numbers.clear(), visited.clear()
    return minimum

def swap(graph, aim1, aim2):
    graph[aim1], graph[aim2] = graph[aim2], graph[aim1]
    for node in graph.keys():
        if aim1 in graph[node]:
            graph[node].remove(aim1)
            graph[node].append(aim2)
        elif aim2 in graph[node]:
            graph[node].remove(aim2)
            graph[node].append(aim1)
    return graph

while True:
    try:
        N, M, I = map(int, input().strip().split())
        ages = [int(x) for x in input().strip().split()]
        graph = {node: [] for node in range(1, N + 1)}
        for _ in range(M):
            X, Y = map(int, input().strip().split())
            graph[X].append(Y)
        for _ in range(I):
            cmd = input().strip().split()
            if len(cmd) == 2: print(fewest(graph, int(cmd[1]), ages))
            else: graph = swap(graph,int(cmd[1]), int(cmd[2]))
    except EOFError: break