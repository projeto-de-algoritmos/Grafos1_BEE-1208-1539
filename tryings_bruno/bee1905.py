def valid_position(x, y):
    if x >= 0 and x < 5 and y >= 0 and y < 5: return True
    return False

def check(graph):
    visited, queue = [[0, 0]], [[0,0]]
    while queue:
        # print(visited)
        u = queue.pop(0)
        x, y = u[0], u[1]
        if x == 4 and y == 4 and not graph[x][y]: return True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != j and valid_position(x + i, y + j) and not (graph[x + i][y + j] or [x+ i, y + j] in visited):
                #    print(x, y, x + i, y + j)
                   visited.append([x + i, y + j]), queue.append([x + i, y + j])
    return False



T = int(input())

for _ in range(T):
    a = input()
    adj = [[int(x) for x in input().strip().split()] for i in range(5)]
    print("COPS" if check(adj) else "ROBBERS")
