import sys

input=sys.stdin.readline
n=int(input())

array=list(map(int,input().split()))
sort_array=sorted(list(set(array)))
dic={}

for i in range(len(sort_array)):
    if not sort_array[i] in dic.keys():
        dic[sort_array[i]]=i

for i in array:
    print(dic[i],end=" ")
