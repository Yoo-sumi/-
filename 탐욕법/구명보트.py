'''def solution(people, limit):
    count=0
    p=len(people)
    min_index=p-1
    array=[]
    people.sort(reverse=True)
    while p>0:
        if min_index in array:
            min_index-=1
            continue
        k=limit-people[min_index]
        array.append(min_index)
        for i in range(len(people)):
            if k-people[i]>=0 and (not i in array):
                k-=people[i]
                array.append(i)#people.pop(i)
                p-=1
                break
        min_index-=1#people.pop()
        count+=1
        if p==0:
            break
        p-=1
    return count'''

'''def solution(people, limit):
    count=0
    people.sort(reverse=True)
    if people[-1]+people[-2]>limit:
        return len(people)
    array=[]
    p=len(people)
    while p!=0:
        for i in range(len(people)-1):
            if people[-1]+people[i]<=limit and not i in array:
                array.append(i)
                p-=1
                break
        people.pop()
        p-=1
        count+=1
    return count'''
def solution(people,limit):
    people.sort()
    count=0
    i=0
    j=len(people)-1
    while i<=j:
        count+=1
        if people[i]+people[j]<=limit:
            i+=1
        j-=1
    return count


print(solution([10,10,10,10,10],10))
# 80 70 50

'''
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
'''