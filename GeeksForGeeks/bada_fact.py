
t=int(input())
while t>0:
    t-=1
    n=int(input())
    op=1
    for i in range(1,n+1):
        op*=i
    print(op)