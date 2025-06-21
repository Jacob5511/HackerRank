t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 1, 2
    total = 0
    while b <= n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    print(total)
