def is_dag(adj: dict):
    keys = list(adj.keys())
    count = [0 for x in keys]
    for key in keys:
        for value in adj[key]:
            count[value - 1] += 1

    i = 0
    while i < len(keys):
        v = -1
        for j in range(len(count)):
            if count[j] == 0:
                v = j
                break
        if v == -1: return False
        count[v] = -1
        for neigh in adj[v + 1]: count[neigh - 1] -= 1
        i += 1
    return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split())
    graph = {node: [] for node in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().strip().split())
        graph[A].append(B)
    print("NAO" if is_dag(graph) else "SIM")
    graph.clear()