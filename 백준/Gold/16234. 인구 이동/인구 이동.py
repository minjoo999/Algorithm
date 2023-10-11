from collections import deque

N, L, R = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def make_union(x, y, num, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    sum = graph[x][y]
    visited[x][y] = num
    cnt = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            else:
                if visited[nx][ny] == 0:
                    now = graph[a][b] - graph[nx][ny]

                    if L <= abs(now) <= R:
                        visited[nx][ny] = num
                        sum += graph[nx][ny]
                        cnt += 1
                        queue.append((nx, ny))
                    else:
                        continue


    if cnt > 1:
        avr = sum // cnt
        return avr
    else:
        return 0



def find_union_avr():
    li = [0 for _ in range(N**2)]

    num = 1
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if num < N**2:
                    li[num] = make_union(i, j, num, visited)
                    num += 1

    
    how = 0
    for i in range(1, N**2):
        avr = li[i]
        if li[i] != 0:

            for j in range(N):
                for k in range(N):
                    if visited[j][k] == i:
                        graph[j][k] = avr

            how += 1

    if how > 0:
        return True
    else:
        return False


days = 0
while True:

    if find_union_avr() == True:
        days += 1

    else:
        break

print(days)
