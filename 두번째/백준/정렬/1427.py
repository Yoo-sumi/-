n=int(input())
array=list(str(n))
array.sort(reverse=True)
for i in array:
    print(i,end="")