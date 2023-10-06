n = int(input())
a, b = map(int, input().split())
m = int(input())

graph_pc = [[] for _ in range(n+1)]
graph_cp = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    graph_pc[parent].append(child)
    graph_cp[child].append(parent)


visited = [0 for _ in range(n+1)]


def dfs(x):
    if x == b:
        return True

    if len(graph_pc[x]) > 0:
        for g in graph_pc[x]:
            if visited[g] == 0:
                visited[g] = visited[x] + 1
                dfs(g)

    if len(graph_cp[x]) > 0:
        for g in graph_cp[x]:
            if visited[g] == 0:
                visited[g] = visited[x] + 1
                dfs(g)

    return False


visited[a] = 1
dfs(a)


if visited[b] == 0:
    print(-1)
else:
    print(visited[b]-1)
