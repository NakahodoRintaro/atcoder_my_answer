a,b,c,k=map(int,open(0).read().split())
while a>=b:
    k-=1
    b*=2
while b>=c:
    k-=1
    c*=2
print("Yes" if k>=0 else "No")
