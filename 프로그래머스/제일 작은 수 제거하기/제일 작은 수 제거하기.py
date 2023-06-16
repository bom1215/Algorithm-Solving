def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr = [-1]
    answer = arr
    return answer