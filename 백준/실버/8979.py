xx,y=map(int,input().split())
array=[]
dic={}
for _ in range(xx):
    a,b,c,d=map(int,input().split())
    array.append((b,c,d,a))
    dic[a]=(b,c,d)
array.sort(key=lambda x:(-x[0],-x[1],-x[2]))

result=1
li=dic[y]
v=0
for a,b,c,d in array:
    if d==y:
        break
    if (a,b,c)==li:
        continue
    result+=1
print(result)




