def solution(num):
    answer = 0
    if num !=1:
        for i in range(500):
            if num % 2 ==0:
                num //=2
            else:
                num *=3
                num+=1
            if num ==1:
                answer= i+1
                break
    if num !=1:
        answer = -1

    return answer