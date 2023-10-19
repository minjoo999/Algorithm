import math
from itertools import permutations

def find_prime_number(n):
    # n1 = math.sqrt(n)
    if n == 0 or n == 1:
        return False
    
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def make_number(x, i):
    result = []
    ns = permutations(x, i)
    
    for n in ns:
        r = ''
        
        for j in range(i):
            r += n[j]
            
        result.append(int(r))
        
    return result
    
    
def solution(numbers):
    
    nums = []
    for i in range(1, len(numbers)+1):
        re = make_number(numbers, i)
        
        for r in re:
            if find_prime_number(r) == True:
                nums.append(r)
                
    
    answer = len(set(nums))
    return answer