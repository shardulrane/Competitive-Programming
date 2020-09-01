# cook your dish here
t=int(input())
while t>0:
    inpt=[int(x) for x in input().split()]
    inpt1=[int(x) for x in input().split()]
    temp=list()
    for i in range(0,len(inpt1)):
        aa=inpt1[i]%inpt[1]
        temp.append(aa)
    print(sum(temp)%inpt[1])
    t-=1