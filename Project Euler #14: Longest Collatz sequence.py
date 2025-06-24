MAX_N = 5000000
collatz_cache = {1: 1}
best_up_to = [0] * (MAX_N + 1)

def collatz_length(n):
    original_n = n
    count = 0
    path = []
    while n not in collatz_cache:
        path.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    count = collatz_cache[n]
    for x in reversed(path):
        count += 1
        if x < MAX_N:
            collatz_cache[x] = count
    return collatz_cache[original_n] if original_n < MAX_N else count

max_len = 1
best_num = 1
for i in range(1, MAX_N + 1):
    length = collatz_length(i)
    if length >= max_len:
        max_len = length
        best_num = i
    best_up_to[i] = best_num

t = int(input())
for _ in range(t):
    n = int(input())
    print(best_up_to[n])
