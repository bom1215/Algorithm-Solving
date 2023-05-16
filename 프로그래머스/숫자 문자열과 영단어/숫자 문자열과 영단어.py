def solution(s):
    answer = 0
    words = ['zero', 'one', 'two', 'three','four','five','six','seven','eight','nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    answer = int(s)
    return answer