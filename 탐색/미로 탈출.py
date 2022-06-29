from collections import deque

sero, garo = map(int, input().split())
lis = []

for i in range(sero):
    tmp = list(map(int, input().split()))
    lis.append(tmp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(graph, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= sero or ny >= garo:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

            if graph[nx][ny] == 0:
                continue

    return graph[sero-1][garo-1]


print(BFS(lis, 0, 0))

