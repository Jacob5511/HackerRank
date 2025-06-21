t = int(input())
for _ in range(t):
    n = int(input())
    max_product = -1
    for a in range(1, n // 3 + 1):
        numerator = n * n - 2 * n * a
        denominator = 2 * (n - a)
        if denominator == 0:
            continue
        if numerator % denominator == 0:
            b = numerator // denominator
            c = n - a - b
            if b > 0 and c > 0 and a * a + b * b == c * c:
                product = a * b * c
                if product > max_product:
                    max_product = product
    print(max_product)
