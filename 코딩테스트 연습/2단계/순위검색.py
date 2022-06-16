def solution(info, query):
    answer = []
    dic={}
    grade={}
    for i in range(len(info)):
        li=info[i].split(" ")
        for s in li[:-1]:
            dic[s]=dic.get(s,[])+[i]
        grade[i]=li[-1]
    for q in query:
        li=q.split(" ")
        temp=[i for i in range(len(info))]
        arr=[]
        for s in li[:-1]:
            if s=='and' or s=='-':
                continue
            a=dic.get(s,[i for i in range(len(info))])
            temp=set(a)&set(temp)
        g=li[-1]
        for t in temp:
            if int(grade[t])>=int(li[-1]):
                arr.append(t)
        answer.append(len(arr))
    return answer