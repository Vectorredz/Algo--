def getPrimes(n):
    primeset = set()
    primeset.add(1)
    p = 2
    m = int(n**.5)
    for x in range(2,m):
        if x not in primeset:
            for i in range(p*p,n+1,p):
                primeset.add(i)
        p += 1
    return primeset
    # return prime 

n,q = [int(x) for x in input().split()]
primes = getPrimes(n)
print(n - len(primes))
for x in range(q):
    num = int(input())
    if num not in primes:
        print(1)
    else:
        print(0)