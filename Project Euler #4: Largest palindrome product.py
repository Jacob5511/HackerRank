palindromes = set()
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            palindromes.add(product)

palindromes = sorted(palindromes)

t = int(input())
for _ in range(t):
    n = int(input())
    # Find largest palindrome less than n
    result = 0
    for p in palindromes:
        if p < n:
            result = p
        else:
            break
    print(result)
