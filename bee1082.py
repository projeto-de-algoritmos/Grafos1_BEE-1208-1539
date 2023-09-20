def bfs(graph: dict):
    visited, queue, components = [], [], []
    for v in graph.keys():
        if not v in visited:
            visited.append(v), queue.append(v)
            components.append([v])
            while queue:
                u = queue.pop(0)
                for w in graph[u]:
                    if not w in visited:
                        visited.append(w), queue.append(w)
                        components[-1].append(w)
    return components

N = int(input())

for i in range(N):
    e, v = map(int, input().strip().split())
    adj = {chr(idx + 97): [] for idx in range(e)}
    for _ in range(v):
        nodes = input().strip().split()
        adj[nodes[0]].append(nodes[1]), adj[nodes[1]].append(nodes[0])
    components = bfs(adj)
    print(f"Case #{i + 1}:")
    for c in components:
        print(",".join(sorted(c)), end=",\n")
    print(f"{len(components)} connected components\n")
    adj.clear()
