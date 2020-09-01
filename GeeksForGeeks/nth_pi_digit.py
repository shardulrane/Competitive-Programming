import math
def sqrt(n,m):
    m1=10**16
    m2=float((n*m1)//m)/m1
    b=(int(m1*math.sqrt(m2))*m)//m1
    n_m=n*m
    while True:
        a=b
        b=(b+n_m//b)//2
        if b==a:
            break
    return b
def power(n):
    if n==0:
        return 1
    r=power(n//2)
    if n%2==0:
        return r*r
    return r*r*10
def pi():
    m=power(100000)
    c=(640320**3)//24
    n=1
    a=m
    sa=m
    sb=0
    while a!=0:
        a*=-(6*n-5)*(2*n-1)*(6*n-1)
        a//=n*n*n*c
        sa+=a
        sb+=n*a
        n+=1
    r=(426880*sqrt(10005*m,m)*m)//(13591409*sa+545140134*sb)
    return r
X=str(pi())
t=int(input())
while t:
    t-=1
    n=int(input())
    print (X[n-1])