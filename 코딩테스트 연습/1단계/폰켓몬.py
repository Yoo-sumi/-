from itertools import combinations
def solution(nums):
    answer = 0
    if len(set(nums))<=int(len(nums)/2):
        answer= len(set(nums))
    else:
        answer= int(len(nums)/2)
    return answer