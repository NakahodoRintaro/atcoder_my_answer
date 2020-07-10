num = int(input())
ans = [int(input()) for _ in range(num)]
pre = ans[0]
for i in range(1,num):
  if ans[i] == pre:
    print('stay')
  elif ans[i] < pre:
    print('down %d' % (pre-ans[i]))
  elif ans[i] > pre:
    print('up %d' % (ans[i] - pre))
  pre = ans[i]
