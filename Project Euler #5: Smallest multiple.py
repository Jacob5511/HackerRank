import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

t = int(input())
for _ in range(t):
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    print(result)
