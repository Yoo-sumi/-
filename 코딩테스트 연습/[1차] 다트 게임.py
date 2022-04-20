def solution(dartResult):
    s=""
    arr=[]
    dic={'S':1,'D':2,'T':3}
    num=1
    for i in dartResult:
        if num==1:
            if i in ['S','D','T']:
                if s:
                    s=pow(int(s),dic[i])
                num=2
                continue
            s+=i
        elif num==2:
            if not i in ['*','#']:
                arr.append(s)
                s=i
            else:
                if i=='*':
                    if arr:
                        arr[-1]*=2
                    arr.append(s*2)
                    s=""
                elif i=='#':
                    arr.append(s*-1)
                    s=""
            num=1
    if s:
        arr.append(s)
    return sum(arr)