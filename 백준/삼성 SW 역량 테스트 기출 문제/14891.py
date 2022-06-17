wheel=[[] for _ in range(4)]
for i in range(4):
    wheel[i]=list(str(input()))
k=int(input())

def rotate(arr,dir):
    arr=list(wheel[arr])
    if dir==1:
        arr=[arr[-1]]+arr[:-1]
    elif dir==-1:
        arr=arr[1:]+[arr[0]]
    return arr
for i in range(k):
    state=[0]*4
    a,b=map(int,input().split())
    state[a-1]=b

    for i in range(4):
        if state[i]!=0:
            for index in range(i-1,-1,-1):
                if state[index]!=0:
                    break
                if wheel[index][2]!=wheel[index+1][6]:
                    state[index]=-state[index+1]
            for index in range(i+1,4):
                if state[index]!=0:
                    break
                if wheel[index-1][2]!=wheel[index][6]:
                    state[index]=-state[index-1]
    for i in range(4):
        wheel[i]=rotate(i,state[i])
result=0
for i in range(4):
    if wheel[i][0]=='1':
        result+=2**i
print(result)
