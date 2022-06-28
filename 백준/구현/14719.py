import sys
input=sys.stdin.readline
answer=0
h,w=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(1,w-1):
    left=max(arr[:i])
    right=max(arr[i+1:])
    if left>arr[i] and right>arr[i]:
        answer+=min(left,right)-arr[i]
print(answer)
