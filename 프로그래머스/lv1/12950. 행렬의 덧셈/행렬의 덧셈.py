def solution(arr1, arr2):
    
    num = len(arr1)
    answer = []
    
    for i in range(num):
        
        li = []
        
        for k in range(len(arr1[0])):
            a = arr1[i][k] + arr2[i][k]
            li.append(a)
        
        answer.append(li)

    return answer