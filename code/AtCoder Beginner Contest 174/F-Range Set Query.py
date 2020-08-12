##写経
def main(N,Q,C,LR,A):
    data = [0]*(N+1)
    def add(i,x):
        i+=1
        while i <= N:
            data[i]+= x
            i+=i&-i 
            #下桁から最初に1が出現するところまで拾う
            #111 -> 1 , 1100 -> 100 , 1010 -> 1
    def sum(a,b):
        r=0
        i=b
        while i>0:
            r+=data[i]
            i-=i&-i
        i=a
        while i>0:
            r-=data[i]
            i-=i&-i
        return r
    p=[-1]*N
    q=0
    a=[0]*Q
    for i in range(N):
        if p[C[i]-1]>=0:
            add(p[C[i]-1],-1)
        p[C[i]-1]=i
        add(i,1)
        while q<Q and LR[A[q]][1]==i+1:
            a[A[q]]=sum(LR[A[q]][0]-1,LR[A[q]][1])
            q+=1
    return a
 
import sys
if sys.argv[-1]=='ONLINE_JUDGE':
    from numba import*
    from numba.pycc import CC
    cc = CC('my_module')
  
    def cc_export(f, signature):
        cc.export(f.__name__, signature)(f)
        return njit(f)
  
    main=cc_export(main,(i8,i8,i8[:],i8[:,:],i8[:]))
    cc.compile()
    exit()
  
def input(): return sys.stdin.buffer.readline()
N,Q=map(int, input().split())
import numpy as np
C=np.array(input().split(),dtype=np.int64)
#print(C)
LR_ = [0] * (Q*2)
for i in range(Q):
    LR_[i*2],LR_[i*2+1] = input().split()
LR=np.array(LR_, dtype=np.int64).reshape(Q,2)
#print(LR)
A=np.argsort(LR[:,1])
 
from my_module import main
print(*main(N,Q,C,LR,A),sep='\n')
