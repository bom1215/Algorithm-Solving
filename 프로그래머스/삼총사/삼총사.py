from itertools import combinations
def solution(number):
    answer = 0
    lis = list(combinations(number,3))
    for i in lis:
        if sum(i)==0:
            answer+=1
    return answer