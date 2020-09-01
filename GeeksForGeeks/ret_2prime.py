def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

tc=int(input())
while tc>0:
    tc-=1
    n=int(input())
    for i in range(2,n):
        if isPrime(i) and isPrime(n-i):
            print(i,(n-i))
            break