k = int(input())
if k%2 == 0 or k%5 == 0:
    print(-1)
    exit()
mod = 7%k
cnt = 1
while mod != 0:
    mod = (mod*10+7) % k
    cnt += 1
print(cnt)
k = int(input())
if k%2 == 0 or k%5 == 0:
    print(-1)
    exit()
mod = 7%k
cnt = 1
while mod != 0:
    mod = (mod*10+7) % k
    cnt += 1
print(cnt)
提出情報
