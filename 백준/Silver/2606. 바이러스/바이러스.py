n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0 for _ in range(n+1)]

cnt = 0


def dfs(x):
    global cnt
    cnt += 1

    if len(graph[x]) > 0:
        for g in graph[x]:
            if visited[g] == 0:
                visited[g] = 1
                dfs(g)
            else:
                continue


visited[1] = 1
dfs(1)

print(cnt-1)

