t=int(input())

while t!=0:
   
    n=int(input())
   
    if n==1:
        print(1)
        print(1,1)
    elif n%2==0:
        print(n//2)
        for i in range(0,n,2):
            print(2,i+1,i+2)
    else:
        print(n//2)
        if n>3:
            print(3,1,2,3)
            for i in range(3,n,2):
                print(2,i+1,i+2)
        elif n==3:
            print(3,1,2,3)
           
           
           
           
   
    t-=1
