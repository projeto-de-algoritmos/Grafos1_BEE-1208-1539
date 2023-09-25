def friends(graph, start, finish, size):
    visited, queue = [0 for _ in range(size)], [start]
    visited[start - 1] = 1
    while queue:
        u = queue.pop(0)
        for neigh in graph[u]:
            if neigh == finish: return True
            elif not visited[neigh - 1]:
                visited[neigh - 1] =1
                queue.append(neigh)
    return False

while True:
    try:
        N, M, Q = map(int, input().strip().split())
        adj = {node: [] for node in range(1, N + 1)}
        for _ in range(M):
            X, Y = map(int, input().strip().split())
            adj[X].append(Y), adj[Y].append(X)
        for _ in range(Q):
            A, B = map(int, input().strip().split())
            print("S" if friends(adj, A, B, N) else "N")
        print("")
    except EOFError: break