MOD = 10**9 + 7

def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = result * base % mod
        base = base * base % mod
        exp //= 2
    return result

def precompute_factorials(limit):
    fact = [1] * (limit + 1)
    inv_fact = [1] * (limit + 1)

    for i in range(1, limit + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    inv_fact[limit] = mod_pow(fact[limit], MOD - 2, MOD)
    for i in range(limit - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    return fact, inv_fact

def nCr(n, r, fact, inv_fact):
    if r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# Input
t = int(input())
m_values = []
n_values = []
max_sum = 0

for _ in range(t):
    m, n = map(int, input().split())
    m_values.append(m)
    n_values.append(n)
    max_sum = max(max_sum, m + n)

# Precompute factorials
fact, inv_fact = precompute_factorials(max_sum)

# Process each test case
for m, n in zip(m_values, n_values):
    print(nCr(m + n, m, fact, inv_fact))
