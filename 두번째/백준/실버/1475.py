import math
n=str(input())
array=[0]*10
for s in n:
    array[int(s)]+=1
if array[6]>array[9]:
    v=array[6]-array[9]
    v=array[9]+math.ceil(v/2)
    array[6]=v
elif array[6]<array[9]:
    v=array[9]-array[6]
    v=array[6]+math.ceil(v/2)
    array[6]=v
array=array[:-1]
print(max(array))
