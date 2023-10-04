N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

    
buildings = 0


def dfs(x, y):
    global buildings
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            buildings += 1
            dfs(nx, ny)


results = []
groups = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            groups += 1
            dfs(i, j)
            if buildings == 0:
                results.append(1)
            else:
                results.append(buildings)
            buildings = 0

print(groups)
results.sort()
for r in results:
    print(r)
