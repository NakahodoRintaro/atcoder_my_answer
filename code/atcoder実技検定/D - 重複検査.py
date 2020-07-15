N=int(input())
numlist=list(range(1,N+1))
dnum=0
nulnum=0
for _ in range(N):
  i = int(input())
  numlist[i-1]=numlist[i-1]-i 
  if numlist[i-1] < 0:
    dnum=i
nulnum=sorted(numlist)[-1]
if dnum==0:
  print('Correct')
else:
  print(dnum,nulnum)
