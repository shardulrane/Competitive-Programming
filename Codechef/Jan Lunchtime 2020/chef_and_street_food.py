# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    temp=[]
    maxx=list()
    for i in range(0,n):
        inpt=[int(x) for x in input().split()]
        temp.append(inpt)
    for j in range(0,n):
        news=temp[j][0]+1
        if(temp[j][1] % news==0):
            tempo=(temp[j][1]//news)*temp[j][2]
            maxx.append(tempo)
        else:
            tempo=(temp[j][1]//news)*temp[j][2]
            maxx.append(tempo)
            
    
    print(max(maxx))
    t-=1