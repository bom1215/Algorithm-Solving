import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    a = np.array(arr1)
    b = np.array(arr2)
    answer = (a@b).tolist()
    
    return answer