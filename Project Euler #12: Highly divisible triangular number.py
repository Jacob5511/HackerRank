import sys
import math

sys.setrecursionlimit(10**7)

factor_cache = {}

def prime_factorization(n):
    if n in factor_cache:
        return factor_cache[n]
    factors = {}
    temp = n
    for i in range(2, int(math.isqrt(n)) + 1):
        while temp % i == 0:
            factors[i] = factors.get(i, 0) + 1
            temp //= i
        if temp == 1:
            break
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    factor_cache[n] = factors
    return factors

def merge_factors(f1, f2):
    merged = f1.copy()
    for p, e in f2.items():
        merged[p] = merged.get(p, 0) + e
    return merged

def divisor_count(factors):
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count

t = int(input())
tests = [int(input()) for _ in range(t)]
max_n = max(tests)
results = {}

k = 1
while len(results) < len(tests):
    if k % 2 == 0:
        f1 = prime_factorization(k // 2)
        f2 = prime_factorization(k + 1)
    else:
        f1 = prime_factorization(k)
        f2 = prime_factorization((k + 1) // 2)
    total_factors = merge_factors(f1, f2)
    div_count = divisor_count(total_factors)
    tri_num = k * (k + 1) // 2
    for n in tests:
        if n not in results and div_count > n:
            results[n] = tri_num
    k += 1

for n in tests:
    print(results[n])
