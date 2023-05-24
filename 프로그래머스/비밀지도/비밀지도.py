def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        a = bin(a)[2:]
        b = bin(b)[2:]
        if len(a) < n:
            a = '0'*(n-len(a))+a
        if len(b) < n:
            b = '0'*(n-len(b))+b
        temp = ''
        for i, j in zip(a,b):
            if i == '0' and j == '0':
                temp +=' '
            else:
                temp +='#'
        answer.append(temp)
                
    
        
        
    return answer