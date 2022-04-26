from itertools import combinations
def solution(relation):
    answer = 0
    index=[i for i in range(len(relation[0]))]
    array=[[] for _ in range(len(relation[0]))]
    for i in relation:
        for j in range(len(i)):
            array[j].append(i[j])
    li=[]
    # 후보키 판별(항목1개)
    for i in range(len(array)):
        if len(array[i])==len(set(array[i])):
            li.append(i)
    answer+=len(li)
    for i in li:
        index.remove(i)

    result=[]
    for num in range(2,len(index)+1):
        li=list(combinations(index,num))
        for i in li:
            temp=[]
            flag=True
            for j in range(len(relation)):
                word=""
                for h in i:
                    word+=relation[j][h]
                if word in temp:
                    flag=False
                    continue
                temp.append(word)
            if flag:
                f=True
                for hh in result:
                    if set(hh).issubset(set(i)):
                        f=False
                        break
                if f:
                    result.append(i)

    return len(result)+answer