import math
def solution(n, m):
    def lcm(n,m):
        for i in range(max(n,m), m*n+1):
            if i%n ==0 and i%m==0:
                return i


    return [math.gcd(n,m), lcm(n,m)]