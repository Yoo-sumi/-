n=int(input())
time=[]
pay=[]
dp=[0]*(n+1)
for _ in range(n):
    a,b=map(int,input().split())
    time.append(a)
    pay.append(b)

for i in range(n):
    dp[i]=max(dp[i],dp[i-1])
    while True:
        if i>n-1:
            break
        index=i+time[i]
        if index>n:
            break
        dp[index]=max(dp[index],dp[i]+pay[i])
        i=index
print(max(dp))