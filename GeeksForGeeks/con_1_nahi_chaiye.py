t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=list()
    arr.append(0)
    arr.append(2)
    arr.append(3)
    if n>2:
        for i in range(3,n+1):
            arr.append((arr[i-1]+arr[i-2]))
        print(arr[-1]%((10**9)+7))
    else:
        print(arr[n])
    