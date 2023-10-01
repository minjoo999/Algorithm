from collections import deque


def solution(maps):
    m = len(maps)
    n = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        D = deque()
        D.append((x, y))

        while D:
            x, y = D.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                    
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    D.append((nx, ny))

        # return maps[n-1][m-1]
        return maps[m-1][n-1]

    answer = bfs(0, 0)

    if answer <= 1:
        return -1
    else:
        return answer
