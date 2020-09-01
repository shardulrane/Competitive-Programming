t=int(input())
while t>0:
    n=int(input())
    arr=[int(x) for x in input().split()]
    k=int(input())
    arr.sort()
    print(arr[k-1])
    
    t-=1
    