def solution(sizes):
    max_arr=[]
    min_arr=[]
    for a,b in sizes:
        max_arr.append(max(a,b))
        min_arr.append(min(a,b))
    return max(max_arr)*max(min_arr)