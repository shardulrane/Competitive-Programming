# cook your dish here
import math
def primeFactors(n):
    pf=[]
    while n % 2 == 0:
      pf.append(2),
      n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
      while n % i== 0:
         pf.append(i)
         n = n / i
    if n > 2:
      pf.append(n)
    return pf

t=int(input())
while t>0:
    x, k = [int(x) for x in input().split()] 
    if len(primeFactors(x))>=k:
        print(1)
    else:
        print(0)
    t-=1