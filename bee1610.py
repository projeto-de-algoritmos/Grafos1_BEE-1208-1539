def is_dag(adj: dict):
    keys = adj.keys()
    count = {node: 0 for node in keys}
    for node in keys:
        for neigh in adj[node]: count[neigh] += 1
    
    queue = [node for node in count if not count[node]]
    for _ in range(len(keys)):
        if not queue: return False
        v = queue.pop(0)
        for neigh in adj[v]:
            count[neigh] -= 1
            if not count[neigh]: queue.append(neigh)
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