
def sieve(N):
    is_primes = [1]*(N+1)
    is_primes[0] = 0
    is_primes[1] = 0

    i = 2
    while i*i <= (N+1):
        if is_primes[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < (N+1):
            is_primes[j] = 0
            j += i

        i += 1
    primes = []
    for i in range(1, N+1):
        if is_primes[i] == 1:
            primes.append(i)
    return primes

def is_prime(n: int, primes: list[int]):
    if n in primes:
        return 1
    else:
        return 0

def primeth(n: int, primes: list[int]):
    if is_prime(n, primes):
        return len(primes)
    else:
        return 0

def main():
    output = []
    i, j = [int(x) for x in input().split()]
    primes: list[int] = sieve(i)

    output.append(primeth(i, primes))
    for i in range(j):
        k = int(input())
        output.append(is_prime(k, primes))

    for result in output:
        print(result)

main()


    



