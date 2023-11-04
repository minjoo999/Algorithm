N = int(input())

dp = [[0]*10 for _ in range(N+1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def count_hill_nums(n):
    sum_dp = sum(dp[n-1])
    res = sum_dp
    dp[n][0] = sum_dp

    for i in range(1, 10):
        res -= dp[n-1][i-1]
        dp[n][i] = res


for j in range(2, N+1):
    count_hill_nums(j)

    
print(sum(dp[N]) % 10007)
