import copy
def solution():
    n,k=map(int,input().split())
    if n==0:
        return -1
    bottle=[1]*n
    count=0
    while len(bottle)>k:
        temp=[]
        index=0
        while index<len(bottle):
            if index+1>=len(bottle):
                temp.append(bottle[index])
                break
            if bottle[index+1]==bottle[index]:
                temp.append(bottle[index]*2)
                index+=2
                continue
            temp.append(bottle[index])
            index+=1
        bottle.sort()
        if len(temp)==len(bottle):
            temp=[]
            flag=True
            for i in range(len(bottle)):
                if flag:
                    temp.append(bottle[i]*2)
                    count+=bottle[i]
                    flag=False
                else:
                    temp.append(bottle[i])
        bottle=copy.deepcopy(temp)
    return count
print(solution())
