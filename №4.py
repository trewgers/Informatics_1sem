f=open('input.txt','r')
lines=f.readlines()
f.close
n=list(map(float,lines[0].split()))
z=lines[1].strip
res=n[0]
for i in n[1:]:
    if z == '+':
        res+=n
    elif z == '-':
        res-=n
    elif z == '*':
        res*=n
    elif z =='/':
        res/=n

f=open("output.txt", "w")
f.write(str(res))
f.close()