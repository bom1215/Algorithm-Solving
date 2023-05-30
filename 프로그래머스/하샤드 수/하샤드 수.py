def solution(x):
    answer = True
    x = str(x)
    ha = 0
    for i in list(x):
        ha += int(i)
    print(ha)
    if int(x) % ha != 0:
        answer = False
    return answer