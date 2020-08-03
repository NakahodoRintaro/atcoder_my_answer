N = int(input())
A = list(map(int, input().split()))
x=1000
for i in range(N - 1):
  s = A[i]
  t = A[i +1]
  if s < t:
    k = x//s
    x %= s
    x += k*t
 
print(x)
