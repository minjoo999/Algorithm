def solution(brown, yellow):
    answer = []
    
    if yellow == 1:
        answer.append(yellow+2)
        answer.append(yellow+2)
        
        
    elif yellow > 1:
        
        for i in range(1, yellow // 2 + 1):

            # i는 세로, j는 가로

            if yellow % i == 0:
                j = yellow // i

                if 4 + i*2 + j*2 == brown:
                    answer.append(j+2)
                    answer.append(i+2)
                    break

    return answer