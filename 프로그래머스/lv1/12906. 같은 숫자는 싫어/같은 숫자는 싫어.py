def solution(arr):
    arr2 = []
    
    arr2.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr2[-1]:
            arr2.append(arr[i])
        else:
            pass
    
    return arr2