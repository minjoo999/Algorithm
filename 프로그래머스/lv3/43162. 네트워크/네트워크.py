def solution(n, computers):
    visited = [False] * n
    
    def dfs(x):
        
        for i in range(n):
            if i != x and computers[x][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)
                
                
    cnt = 0
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(j)
            cnt += 1
            
                
    return cnt