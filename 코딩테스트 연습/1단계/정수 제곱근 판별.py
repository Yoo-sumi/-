import math
def solution(n):
    if pow(int(math.sqrt(n)),2)==n:
        return (1+math.sqrt(n))**2
    return -1