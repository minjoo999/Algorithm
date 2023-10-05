import sys
from collections import deque

input = sys.stdin.readline


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F)]


def bfs():
    queue = deque([S-1])
    visited[S-1] = 1

    while queue:
        x = queue.popleft()
        if x == G-1:
            break

        for nx in (x - D, x + U):
            if 0 <= nx < F and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)


bfs()
if S == G:
    print(0)
else:
    if visited[G-1] == 0:
        print("use the stairs")
    else:
        print(visited[G-1]-1)
