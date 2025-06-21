t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    num = input().strip()

    max_product = 0

    for i in range(n - k + 1):
        digits = num[i:i+k]
        if '0' in digits:
            continue  # skip segments with zero
        product = 1
        for d in digits:
            product *= int(d)
        if product > max_product:
            max_product = product

    print(max_product)
