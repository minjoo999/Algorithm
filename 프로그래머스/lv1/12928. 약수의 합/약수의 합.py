def solution(n):
    
    nums = []
    
    for i in range(1, n+1):
        if n % i == 0:
            nums.append(i)
    answer = sum(nums)

    return answer