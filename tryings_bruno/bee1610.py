def is_dag(graph: dict):
    counts = [x for sublist in graph.values() for x in sublist]
    values = {node: 0 for node in graph.keys()}
    for item in counts: values[item] += 1
    values = [[x[0], x[1]] for x in list(values.items())]
    i = 0
    while (i < len(graph.keys())) and values:
        i += 1
        v = values[0]
        if v[1] != 0: return False
        values.pop(0)
        for i in range(len(values)): values[i][1] -= 1
        values = sorted(values, key=lambda x: x[1])
    return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split())
    adj = {x: [] for x in range(1, N + 1)}
    for _ in range(M):
        A, B = map(int, input().strip().split())
        adj[A].append(B)
    print("NAO" if is_dag(adj) else "SIM")
    adj.clear()