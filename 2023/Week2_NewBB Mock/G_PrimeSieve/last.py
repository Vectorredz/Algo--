def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n, q = [int(x) for x in input().split()]

    primes = sum(is_prime(i) for i in range(2, n+1))
    print(abs(primes))

    for _ in range(q):
        nums = int(input())
        if is_prime(nums):
            print(1)
        else:
            print(0)
    
main()
