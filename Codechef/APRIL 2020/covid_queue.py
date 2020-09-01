# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    exp=int(n/6)+1
    inpt=[int(x) for x in input().split()]
    if inpt.count(1)==1:
        print("YES")
    else:
        opp=[]
        for i in range(0,n):
            if inpt[i]==1:
                opp.append(i)
        oo="YES"
        for i in range(0,(len(opp)-1)):
            if ((opp[i+1]-opp[i])<6):
                oo="NO"
                break
        print(oo)        
    t-=1