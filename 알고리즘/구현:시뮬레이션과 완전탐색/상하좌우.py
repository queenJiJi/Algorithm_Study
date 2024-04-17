n=int(input())
ss=input().split()

x,y=1,1
dx= [0,0,1,-1]
dy= [-1,1,0,0]
dir =['L','R','U','D']
for s in ss:
  nx,ny=-1,-1
  for i in range(len(dir)):
    if dir[i] == s:
      nx=x+dx[i]
      ny=y+dy[i]
    # noinspection PyUnboundLocalVariable
      if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    x,y=nx,ny
print(x,y)
