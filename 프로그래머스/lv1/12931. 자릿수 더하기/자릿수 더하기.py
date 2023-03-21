def solution(n):
    m = str(n)
    answer = 0
    
    for i in range(len(m)):
        answer += int(m[i])

    return answer