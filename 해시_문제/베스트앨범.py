def solution(genres, plays):
    answer = []
    data={}
    index={}
    for i in range(len(genres)):
        data[genres[i]]=data.get(genres[i],[])+[plays[i]]
        index[plays[i]]=index.get(plays[i],[])+[i]
    a=[]
    for i in data.keys():
        a.append(sum(data[i]))
    a.sort(reverse=True)
    for i in a:
        for j in data.keys():
            if sum(data[j])==i:
                num=data[j]
                num=sorted(num,reverse=True)
                array=[]
                for h in range(len(num)):
                    if h==2:
                        break
                    a=sorted(index[num[h]],reverse=True)
                    array.append((num[h],a.pop()))
                    index[num[h]]=a
        answer+=array
    result=[]
    for i in answer:
        result.append(i[1])

    return result

print(solution(["classic", "pop", "classic", "pop", "classic", "classic"],[400, 600, 150, 600, 500, 500]))