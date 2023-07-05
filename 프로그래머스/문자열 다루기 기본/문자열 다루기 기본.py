def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except:
            return False
    else:
        return False
