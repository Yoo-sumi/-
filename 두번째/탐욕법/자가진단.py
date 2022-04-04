arr=[3,2,3,3,3,4,4]
print(set(arr))
flag=[]
result=[]
for i in arr:
    if arr.count(i)>1 and not i in flag:
        result.append(arr.count(i))
        flag.append(i)
if not result:
    result.append(-1)
print(result)