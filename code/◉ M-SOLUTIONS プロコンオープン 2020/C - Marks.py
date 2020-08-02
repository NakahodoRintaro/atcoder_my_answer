from sys import stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
L = [int(_) for _ in stdin.readline().rstrip().split()]
for i in range(K+1, N+1):
	if L[i-K-1] < L[i-1]:
		print("Yes")
	else:
		print("No")
