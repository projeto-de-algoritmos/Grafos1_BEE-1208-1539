def bfs(graph: dict):
    visited, components, queue = [], [], []
    for node in graph.keys():
        if not node in visited:
            visited.append(node), queue.append(node)
            components.append([node])
            while queue:
                u = queue.pop(0)
                for n in graph[u]:
                    if not n in visited:
                        visited.append(n), queue.append(n), components[-1].append(n)
    return len(components) - 1

T = int(input())

for i in range(T):
    N = int(input())
    M = int(input())
    roads = {road: [] for road in range(N)}
    for _ in range(M):
        x, y = map(int, input().strip().split())
        x, y = x - 1, y - 1
        roads[x].append(y), roads[y].append(x)
    total = bfs(roads)
    print(f"Caso #{i+1}: a promessa foi cumprida" if not total else f"Caso #{i+1}: ainda falta(m) {total} estrada(s)")
    roads.clear()