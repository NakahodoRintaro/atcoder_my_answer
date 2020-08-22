N = int(input())
A = [int(i) for i in input().split()]
K = 0
for i in range(N-1):
  if A[i] > A[i+1]:
    S = A[i] - A[i+1]
    # リストの前の最大値を取得して比較しないといけない。
    A[i+1] += S
    K += S
  else:
    pass
print(K)
