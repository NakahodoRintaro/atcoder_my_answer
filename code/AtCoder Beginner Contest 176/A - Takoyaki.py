import math
N, X, T = map(int, input().split())
S = math.ceil(N/X)
Ans = S * T
print(Ans)
