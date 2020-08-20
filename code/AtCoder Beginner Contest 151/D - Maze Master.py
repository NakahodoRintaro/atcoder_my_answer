h,w=map(int,input().split())
g=[input() for _ in range(h)]
from collections import *
def bfs(sx,sy):
  d=[[-1]*w for _ in range(h)]
  d[sx][sy]=0
  q=deque([(sx,sy)])
  while q:
    x,y=q.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.' and d[nx][ny]<0:
        r=d[nx][ny]=d[x][y]+1
        q.append((nx,ny))
  return r
print(max(bfs(sx,sy) for sx in range(h) for sy in range(w) if g[sx][sy]=='.'))
h,w=map(int,input().split())
g=[input() for _ in range(h)]
from collections import *
def bfs(sx,sy):
  d=[[-1]*w for _ in range(h)]
  d[sx][sy]=0
  q=deque([(sx,sy)])
  while q:
    x,y=q.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.' and d[nx][ny]<0:
        r=d[nx][ny]=d[x][y]+1
        q.append((nx,ny))
  return r
print(max(bfs(sx,sy) for sx in range(h) for sy in range(w) if g[sx][sy]=='.'))
