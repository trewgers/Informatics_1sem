G = int(input())
s = input().strip()

L = len(s) // G
result = ""

for i in range(G):
    group = s[i*L : (i+1)*L]
    result += group[::-1]
print(result)