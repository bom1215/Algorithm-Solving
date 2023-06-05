def solution(s):
    answer = True
    cp = 0
    cy = 0 
    s = s.lower()
    for i in s:
        if i == 'p':
            cp+=1
        elif i == 'y':
            cy+=1
    if cp != cy:
        answer = False
            
    

    return answer