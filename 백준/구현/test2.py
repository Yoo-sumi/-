arr=[1,2,3]

def comb(arr,n):
    result=[]
    if n>len(arr):
        return result
    if n==1:
        for i in arr:
            result.append([i])
    elif n>1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result
def perm(arr,n):
    result=[]
    if n>len(arr):
        return result
    if n==1:
        for i in arr:
            result.append([i])
    elif n>1:
        for i in range(len(arr)):
            ans=[i for i in arr]
            ans.remove(arr[i])
            for p in perm(arr,n-1):
                result.append([arr[i]]+p)
    return result

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i]+arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result
print(combination(arr,3))
print(permutation(arr,3))