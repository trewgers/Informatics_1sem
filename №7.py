n = int(input())
total = n * (n + 1) // 2

A = []
for i in range(n - 1):
    A.append(int(input()))

for x in A:
    total -= x

print(total)
