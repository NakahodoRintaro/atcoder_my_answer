n, m, k = map(int,input().split())
s = sum(list(map(int, input().split())))
r = k*n - s
if r<0:
    print(0)
elif r>m:
    print(-1)
else:
    print(r)
