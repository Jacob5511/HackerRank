t = int(input())
for _ in range(t):
    n = int(input())
    num = 2 ** n
    s = sum(int(d) for d in str(num))
    print(s)
