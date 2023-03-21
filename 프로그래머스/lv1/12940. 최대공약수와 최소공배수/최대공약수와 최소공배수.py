def solution(n, m):
    li = sorted([n, m])
    answer = []
    
    # 공약수
    ans1 = []
    for i in range(1, li[0]+1):
        if (li[0] % i == 0) & (li[1] % i == 0):
            ans1.append(i)
    answer.append(ans1[-1])
    
    # 공배수
    ans = answer[0]
    if ans == 1:
        answer.append(li[0] * li[1])
    else:
        num = ans * (li[0] // ans) * (li[1] // ans)
        answer.append(num)
    
    return answer