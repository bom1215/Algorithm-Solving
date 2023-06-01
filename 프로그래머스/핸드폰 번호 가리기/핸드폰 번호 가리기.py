def solution(phone_number):
    answer = ''
    a = list(phone_number)
    a.reverse()
    for i in range(len(a)):
        if i >=4:
           a[i] = '*'
    a.reverse()
    answer = ''.join(a)
    return answer