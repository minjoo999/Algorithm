from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0))
while queue:

    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if graph[nx][ny] == 0 or graph[nx][ny] > 1:
            continue

        if graph[nx][ny] == 1:
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
    
print(graph[N-1][M-1])
