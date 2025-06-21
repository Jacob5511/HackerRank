def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

primes = sieve(200000)

t = int(input())
for _ in range(t):
    n = int(input())
    print(primes[n - 1])
