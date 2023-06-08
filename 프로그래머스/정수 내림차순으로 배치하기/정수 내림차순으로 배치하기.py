def solution(n):
    answer = 0
    lis = sorted(list(str(n)), reverse=True)
    answer = int(''.join(lis))
    return answer