import sys
sys.setrecursionlimit(100000)

N = int(input())
area = []

min_areas = []
max_areas = []

for _ in range(N):
    li = list(map(int, input().split()))
    area.append(li)
    min_areas.append(min(li))
    max_areas.append(max(li))

# 높이 범위 구하기
min_x = min(min_areas)
max_x = max(max_areas)


def dfs(x, y, std):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if area[nx][ny] > std and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, std)

    return False


now_x = min_x

ans = 1
while now_x < max_x:
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > now_x:

                cnt += 1
                visited[i][j] = 1
                dfs(i, j, now_x)

    ans = max(ans, cnt)
    now_x += 1

print(ans)
