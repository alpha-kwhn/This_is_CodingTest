def DFS(graph, x, y, sero, garo):
    if x <= -1 or x >= sero or y >= garo or y <= -1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(graph, x-1, y, sero, garo)
        DFS(graph, x, y-1, sero, garo)
        DFS(graph, x+1, y, sero, garo)
        DFS(graph, x, y+1, sero, garo)
        return True
    return False


sero, garo = map(int, input().split())

lis = []
for i in range(sero):
    tmp = list(map(int, input().split()))
    lis.append(tmp)


sums = 0
for i in range(sero):
    for j in range(garo):
        if DFS(lis, i, j, sero, garo):
            sums += 1

print(sums)