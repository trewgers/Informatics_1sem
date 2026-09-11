N=input()
b=int(input())
c=int(input())
m=len(N)
l=0
for i in range(m):
    k=int(N[i])*(b**(m-1-i))
    l+=k
print(l)
A=[]
while l>c:
    A.append(l%c)
    l //= c
A.append(l)
S=[]
for i in range(len(A)):
    S.append(A[-1*(i+1)])
q=''
for i in range(len(S)):
    q+=str(S[i])
print(q)