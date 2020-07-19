n=int(input())
x=input()
t=int(x,2)
c=x.count('1')
a=t%-~c
b=0 if c<2 else t%~-c
for i in range(n):
  if int(x[i]):
    if c<2: print(0); continue
    else: t=(b-pow(2,n-i-1,c-1))%~-c
  else: t=(a+pow(2,n-i-1,c+1))%-~c
  z=1
  while t:
    d=bin(t).count('1')
    t%=d
    z+=1
  print(z)
