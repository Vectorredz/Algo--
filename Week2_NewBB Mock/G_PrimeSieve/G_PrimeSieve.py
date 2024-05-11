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

def is_prime(n: int):
    num = 2
    factors: list[int] = []
    for _ in range(1, n+1):
        if n % num == 0:
            factors.append(num)
            num += 1
        else:
            num += 1
    return factors


def checker(n: int):
    if len(is_prime(n)) == 1:
        return 1
    else:
        return 0
    
def primeth(n: int):
    length: list[int] = []
    nums  = list(map(lambda x: x, range(n+1)))
    for i, j in enumerate(nums):
        if checker(j):
            length.append(j)
    return len(length)

print(primeth(1229))
