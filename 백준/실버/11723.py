import sys
input=sys.stdin.readline
n=int(input())
array=[]
for _ in range(n):
    li=input().split()
    a=str(li[0])
    if len(li)==2:
        b=int(li[1])
    if a=="add":
        if not b in array:
            array.append(b)
    elif a=="remove":
        if b in array:
            array.remove(b)
    elif a=="check":
        if b in array:
            print(1)
        else:
            print(0)
    elif a=="toggle":
        if b in array:
            array.remove(b)
        else:
            array.append(b)
    elif a=="all":
        array=[i for i in range(1,21)]
    elif a=="empty":
        array=[]
