def solution(msg):
    answer = []
    dic={}
    num=27
    for i in range(65,91):
        dic[chr(i)]=i-64
    index=0
    while index<len(msg):
        s=list(msg[index:])
        while s:
            if "".join(s) in dic.keys():
                answer.append(dic["".join(s)])
                index+=len("".join(s))
                break
            s.pop()
        if index<len(msg):
            dic["".join(s)+msg[index]]=num
            num+=1
    return answer