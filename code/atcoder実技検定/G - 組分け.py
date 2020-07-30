def iter_p_adic(p, n):
    from itertools import product
    tmp = [range(p)] * n
    return product(*tmp)
 
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n - 1):
    A = [int(i) for i in input().split()]
    for j in range(len(A)):
        graph[i][j + i + 1] = A[j]
        graph[j + i + 1][i] = A[j]
 
iterator = iter_p_adic(3, n)
ans = -(10 ** 9)
for idxs in iterator:
    point = 0
    group = [[] for _ in range(3)]
    for index, v in enumerate(idxs):
        for prev in group[v]:
            point += graph[prev][index]
        group[v].append(index)
    ans = max(ans, point)
print(ans)
