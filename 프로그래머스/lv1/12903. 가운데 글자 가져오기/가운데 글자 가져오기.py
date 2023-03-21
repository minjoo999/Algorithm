def solution(s):
    
    num = len(s)
    
    if num % 2 == 0:
        chars = s[(num // 2) - 1] + s[num // 2]
        return chars
    
    else:
        return s[num // 2]