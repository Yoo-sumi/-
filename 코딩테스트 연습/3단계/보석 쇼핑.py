def solution(gems):
    dic={gems[0]:1}
    start,end=0,0
    n=len(set(gems))
    if n==1:
        return [1,1]
    size=len(gems)
    answer=[0,len(gems)-1]
    while start<size and end<size:
        if len(dic.keys())==n:
            if end-start<answer[1]-answer[0]:
                answer=[start,end]
            if dic.get(gems[start],-1)!=-1:
                dic[gems[start]]-=1
                if dic[gems[start]]==0:
                    del dic[gems[start]]
            start+=1
        else:
            end+=1
            if end>=size:
                continue
            dic[gems[end]]=dic.get(gems[end],0)+1
    return [answer[0]+1,answer[1]+1]