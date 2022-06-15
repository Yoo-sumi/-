def solution(n):
    ans=0
    while n!=0:
        if n%2==0:
            n//=2
        else:
            v=n//2
            ans+=n-2*v
            n=v*2
    return ans