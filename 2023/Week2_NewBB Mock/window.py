def primeSieve(n, X, window=10**6): 
    primes     = []       
    primeCount = 0        
    flags      = list(X)  
    base       = 1        
    isPrime    = [False]+[True]*(window-1)
    
    def flagPrimes():
        flags[:] = [isPrime[x-base]*1 if x in range(base,base+window) else x
                    for x in flags]
    for p in (2,*range(3,n+1,2)):       
        if p >= base+window:            
            flagPrimes()                
            isPrime = [True]*window     
            base    = p                 
            for k in primes:            
                if k>base+window:break
                i = (k-base%k)%k + k*(k==p)  
                isPrime[i::k] = (False for _ in range(i,window,k))
        if not isPrime[p-base]: continue
        primeCount += 1                 
        if p*p<=n:primes.append(p)      
        isPrime[p*p-base::p] = (False for _ in range(p*p-base,window,p))

    flagPrimes()
    return primeCount,flags  

def main():
    n, q = [int(x) for x in input().split()]
    X = [0] * (n+1)

    primeCount, flags = primeSieve(n, X)
    print(abs(primeCount))

    for _ in range(q):
        nums = int(input())
        if flags[nums] == 1:
            print(1)
        else:
            print(0)
    
main()
