arr=[7,4,5,2,6,3,8,1]

def sort(arr):
    temp=[]
    if len(arr)==1:
        return arr
    index=len(arr)//2
    a=sort(arr[:index])
    b=sort(arr[index:])
    a.reverse()
    b.reverse()
    while len(a)>0 and len(b)>0:
        if a[-1]<b[-1]:
            temp.append(a.pop())
        else:
            temp.append(b.pop())
    if a:
        a.reverse()
        temp+=a
    if b:
        b.reverse()
        temp+=b
    print(temp)
    return temp
print(sort(arr))