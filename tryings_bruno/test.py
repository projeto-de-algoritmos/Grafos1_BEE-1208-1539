def is_dag(adj: dict):
    keys = list(adj.keys())
    incoming = [0 for x in adj.keys()]
    for key in keys:
        for value in adj[key]:
            incoming[value - 1] += 1
    # print(incoming, adj)

    i = 0
    while i < len(keys):
        if not 0 in incoming: return False
        v = incoming.index(0)
        for i in range(len(incoming)):
            if (i + 1) in adj[v + 1]: incoming[i] -= 1
        incoming.pop(v)
        keys.pop(v)
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