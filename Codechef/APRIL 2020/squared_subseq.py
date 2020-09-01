t=int(input())

while t!=0:
   
    n=int(input())
    lst=[int(x) for x in input().split()]
    nlst=[]
    for i in lst:
        if i%4==0:
            nlst.append(2)
        elif i%2!=0:
            nlst.append(0)
        else:
            nlst.append(1)
    cnt=0
    pos=0
    pose=0
    ocnt=0
    ecnt=0
    prec=0
    for i in range(n):
        if nlst[i]==2:
            temp1=(ocnt*(ocnt+1))//2
            cnt+=temp1
            temp = (i-pos+1)*(n-i)
            cnt+=abs(temp)
            pos=i+1
            pose=i
            ocnt=0
            ecnt=0
            #print(i,pos,pose,ocnt,ecnt,cnt)
        elif nlst[i]==0:
            ocnt+=1
            if i == n-1:
                temp= ocnt*(ocnt+1)//2
                cnt+=abs(temp)
            ecnt=0
            #print(i,pos,pose,ocnt,ecnt,cnt)
        else:
            ecnt+=1
            temp1=(ocnt*(ocnt+1))//2
            cnt+=temp1
            if nlst[pose]==2:
                pose=i
            elif ecnt>=2:
                temp = (i-pos)*(n-i)
                cnt+=abs(temp)
                ecnt-=1
                pos=i
            elif nlst[pose]==1 and pose!=i:
                temp = i-pos-ocnt
                cnt+=temp*(n-i)
                pos=i-ocnt
            pose=i
            ocnt=0
            #print(i,pos,pose,ocnt,ecnt,cnt)
    print(cnt)
    t-=1