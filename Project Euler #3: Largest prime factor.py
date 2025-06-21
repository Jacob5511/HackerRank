t = int(input())
for _ in range(t):
    n = int(input())
    while n % 2 == 0:
        n //= 2
        last_factor = 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
            last_factor = i
        i += 2
    if n > 2:
        last_factor = n
    print(int(last_factor))
