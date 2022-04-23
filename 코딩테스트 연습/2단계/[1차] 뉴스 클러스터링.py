import math
def sum_AB(A,B):
    r=set(A+B)
    answer=[]
    for i in r:
        answer.append(max(A.count(i),B.count(i)))
    return sum(answer)
def inter_AB(A,B):
    r=[]
    answer=[]
    for i in A:
        if i in B:
            if not i in r:
                r.append(i)
    for i in r:
        answer.append(min(A.count(i),B.count(i)))
    return sum(answer)
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    A,B=[],[]
    for i in range(0,len(str1)-1):
        flag=True
        for j in str1[i:i+2]:
            if not 97<=ord(j)<=122:
                flag=False
                break
        if flag:
            A.append(str1[i:i+2])
    for i in range(0,len(str2)-1):
        flag=True
        for j in str2[i:i+2]:
            if not 97<=ord(j)<=122:
                flag=False
                break
        if flag:
            B.append(str2[i:i+2])
    x=0
    y=0
    if len(A)>=len(B):
        x=inter_AB(A,B)
    else:
        x=inter_AB(B,A)
    y=sum_AB(A,B)
    if x==y==0:
        return math.trunc(1*65536)
    return math.trunc((x/y)*65536)