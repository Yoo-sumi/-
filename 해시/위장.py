def solution(clothes):
    answer = 0
    dic={}
    for i in clothes:
        dic[i[1]]=dic.get(i[1],0)+1
    s=1
    for i in dic.keys():
        s*=(dic[i]+1)
    answer=s-1
    return answer
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]