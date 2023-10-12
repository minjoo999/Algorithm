from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    queue = deque([(x, y)])

    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    melt = []

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            else:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    melt.append([nx, ny])

    return melt


cnt = 0
cakes = 0
while True:

    m = bfs(0, 0)
    if len(m) > 0:
        cakes = len(m)
        for a in m:
            i, j = a
            graph[i][j] = 0
        cnt += 1
        cakes = len(m)
    else:
        break


print(cnt)
print(cakes)
