arr=[1,2,3,3,3,3,4,4]
#arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
#arr=[3, 5, 7, 9, 1]

"""arr.sort()
se=set(arr)
count=[]
for i in se:
    a=arr.count(i)
    if a!=1:
        count.append(a)
if count:
    print(count)
else:
    print([-1])"""

num=[0]*101
for i in arr:
    num[i]+=1
count=[]
for i in num:
    if i>1:
        count.append(i)
if count:
    print(count)
else:
    print([-1])