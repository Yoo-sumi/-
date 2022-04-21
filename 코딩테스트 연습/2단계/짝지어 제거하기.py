def solution(s):
    result=[]
    for i in s:
        if result:
            if result[-1]==i:
                result.pop()
                continue
        result.append(i)
    if result:
        return 0
    return 1