def solution(id_list, report, k):
    answer = [0]*len(id_list)
    count={}
    email={}
    index={}
    for i in range(len(id_list)):
        index[id_list[i]]=i

    for i in report:
        a,b=map(str,i.split())
        if not index[a] in email.get(b,[]):
            email[b]=email.get(b,[])+[index[a]]
            count[b]=count.get(b,0)+1
    for i in count.keys():
        if count[i]>=k:
            for j in email[i]:
                answer[j]+=1

    return answer