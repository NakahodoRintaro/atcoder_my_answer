import sys
 
 
def input():
    return sys.stdin.readline().rstrip()
 
 
 
def main():
    N = int(input())
 
    dp = [0] * (N + 1)
    rt = int(N ** 0.5) + 1
    for i in range(1, rt):
        ii = i ** 2
        for j in range(1, i+1):
            iji = ii + j **2 + i * j
 
            if iji + 1 + i + j > N:
                break
            for k in range(1, j+1):
                case = iji + k**2 + i * k + j * k
                l =6
                if i == j or j == k:
                    l = 3
                    if i == k:
                        l = 1
                if case <= N:
                    dp[case] += l
                else:
                    break
 
    print(*dp[1:N + 1], sep="\n")
 
 
if __name__ == "__main__":
    main()
