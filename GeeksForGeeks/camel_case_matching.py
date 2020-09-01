tc=int(input())
while tc>0:
    n=int(input())
    l=list(input().split())
    s=input()
    d=[]
    for i in l:
        count=0
        a=''
        for j in i:
            if(j.isupper()):
                a=a+j
            if(a==s):
                count+=1
        if(count>0):
            d.append((i,a))
    d=sorted(d,key=lambda x:x[1])
    if(len(d)>0):
        for i in d:
            print(i[0],end=" ")
    else:
        print("No match found",end="")
    print()
    
    tc-=1