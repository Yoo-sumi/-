'''array=['A','E','I','O','U']
temp=[]
def dfs(arr):
    global array
    answer=0
    temp.append("".join(arr))
    if len(arr)==5:
        return 1 ㅏ
    for i in range(5):
        answer+=dfs(arr+[array[i]])
    return answer
def solution(word):
    global array,temp
    for i in range(5):
        dfs([array[i]])

    return temp.index(word)+1'''
from itertools import product
def solution(word):
    answer = 0
    dic={}
    arr=['A','E','I','O','U']
    arr.sort()
    index=0
    li=[]
    for i in range(1,len(arr)+1):
        li+=list(product(arr,repeat=i))
    for i in range(len(li)):
        li[i]="".join(li[i])
    li.sort()

    return li.index(word)+1