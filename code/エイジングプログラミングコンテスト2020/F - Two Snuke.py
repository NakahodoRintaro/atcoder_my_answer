import math
MOD = 10**9+7
 
def resolve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        r = 0
        for i in range((N-5)%2, 12, 2):
            r += math.comb(11,i) % MOD * math.comb((N-i+25)//2, 15) % MOD
        print(r%MOD)
    return
resolve()
