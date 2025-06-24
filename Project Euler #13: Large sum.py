t = int(input())
total = 0

for _ in range(t):
    number = input().strip()
    total += int(number)

print(str(total)[:10])
