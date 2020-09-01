# cook your dish here
t=int(input())
while t>0:
    N,a,b,c = map(int, input().split()) 
    inpt=[int(x) for x in input().split()]
    close=int(inpt[min(range(len(inpt)), key = lambda i: abs(inpt[i]-b))])
    time=0
    minn=min(inpt)
    tt=[]
    for i in range(0,len(inpt)):
        temp=abs(b-inpt[i])+c+abs(a-inpt[i])
        tt.append(temp)
    print(min(tt))
    t-=1