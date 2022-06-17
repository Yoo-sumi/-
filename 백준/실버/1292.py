a,b=map(int,input().split())
num=1
array=[]
while True:
    if len(array)>b:
        break
    for i in range(num):
        array.append(int(num))
    num+=1
result=0
for i in range(a-1,b):
    result+=array[i]
print(result)

