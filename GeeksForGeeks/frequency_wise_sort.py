from collections import Counter
t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=[int(x) for x in input().split()]
    aa=dict(Counter(arr))
    aa=sorted(aa.items(),reverse=True ,key=lambda item: item[1])
    op=""
    for x in aa:
        tt=(str(x[0])+" ")*x[1]
        print(tt,end="")
    print()
    