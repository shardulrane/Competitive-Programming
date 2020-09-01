from random import randint
t=int(input())

while t!=0:
    n,m,k=map(int,input().split())
   
    for i in range(n):
        lst=[int(x) for x in input().split()]
        value = randint(1,m)
        print(value,end=" ")
           
   
   
    t-=1