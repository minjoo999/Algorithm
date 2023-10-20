from itertools import permutations

def count_number(std, lis):
    cnt = 0
    
    for li in lis:
        a, b = li[0], li[1]
        if std < a:
            break
        else:
            std -= b
            cnt += 1
            
    return cnt


def solution(k, dungeons):
    
    li = permutations(dungeons)
    result = []
    
    for l in li:
        r = count_number(k, l)
        result.append(r)
    
    answer = max(result)
    return answer