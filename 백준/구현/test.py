n=int(input())
count=0
result=[]
def solve(n, start,end,mid) :
    global result,count
    if (n == 1):
        result.append([start,end])
        return

    solve(n - 1, start,mid,end);
    count+=1
    result.append([start,end])
    solve(n - 1, mid,end,start);



solve(n, 1, 3,2)
print(count)
for i in result:
    print(i[0],i[1])
