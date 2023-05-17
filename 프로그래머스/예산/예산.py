def solution(d, budget):
    answer = 0
    d = sorted(d)
    s = []
    for i in range(len(d)):
        if sum(s)+d[i] <= budget:
            s.append(d[i])
        else:
            break
    answer = len(s)
    return answer