# n: the num input
# q: number of nums ff.
# identify the given number's prime standing

# define prime checker

# prime factorization
"""
def is_prime(n: int):
    num = 2
    factors: list[int] = []
    for _ in range(1, n+1):
        if n % num == 0:
            factors.append(num)
            n //= num
        else:
            num += 1

    return factors
"""


def sieve(n: int):
    is_prime = [1]*n
    # We know 0 and 1 are composites
    is_prime[0] = 0
    is_prime[1] = 0
    p = 2
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <=n:
        # If we already crossed out this number, then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < n:
            # Cross out this as it is composite
            is_prime[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1
    for i in range(2, n+1):
        if is_prime[i] == 1:
            is_prime.append(i)
    return is_prime

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

