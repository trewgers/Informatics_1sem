f = open('input.txt', 'r')
lines = f.readlines()
f.close()

n = lines[0].split()
z = lines[1].strip()
m = int(lines[2].strip())



def to_dec(num, base):
    res = 0
    for ch in num.upper():
        res = res * base + SYMBOLS.index(ch)
    return res



def from_dec(num, base):
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if num == 0:
        return "0"

    res = ""
    while num > 0:
        res = symbols[num % base] + res
        num //= base

    return res

for i in range(len(n)):
    n[i] = to_dec(n[i], m)


res = n[0]

for i in n[1:]:
    if z == '+':
        res += i

    elif z == '-':
        res -= i

    elif z == '*':
        res *= i

    elif z == '/':
        res /= i

res = int(res)
res = from_dec(res, m)

f = open("output.txt", "w")
f.write(str(res))
f.close()