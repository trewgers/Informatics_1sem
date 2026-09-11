A = list(map(float,input().split()))
d=1.0
for x in A:
    d*=x
g=d**(1/len(A))
print(g)