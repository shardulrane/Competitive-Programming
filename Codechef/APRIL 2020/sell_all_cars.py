# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    inpt=[int(x) for x in input().split()]
    inpt.sort(reverse=True)
    pro=0
    for i in range(0,n):
        temp=inpt[i]-i
        if temp<=0:
            pro+=0
        else:
            pro+=temp
        
    print(pro%1000000007)
    t-=1