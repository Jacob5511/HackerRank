def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

t = int(input())
ns = [int(input()) for _ in range(t)]
max_n = max(ns)

is_prime = sieve(max_n)

prefix_sum = [0] * (max_n + 1)
current_sum = 0
for i in range(2, max_n + 1):
    if is_prime[i]:
        current_sum += i
    prefix_sum[i] = current_sum

for n in ns:
    print(prefix_sum[n])
