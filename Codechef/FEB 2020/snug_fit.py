# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    inpt=[int(x) for x in input().split()]
    inpt.sort()
    inpt1=[int(x) for x in input().split()]
    inpt1.sort()
    temp=list()
    for i in range(0,n):
        if inpt[i]>inpt1[i]:
            temp.append(inpt1[i])
        else:
            temp.append(inpt[i])
    print(sum(temp))
    t-=1