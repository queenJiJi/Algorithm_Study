n = int(input())

tmp = [[0]*n for _ in range(n)]

r,c = 0,0
num = 1
dir = 0

while num<=n**2:
  tmp[r][c] = num

  for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
    print(dr,dc)
    nr,nc= r+dr, c+dc
    
    if nr<0 or nc<0 or nc>=n or nr>=0 or tmp[nr][nc]!=0:
      dir = (dir+1)%4
      nr=r+dr
      nc=c+dc
    r,c = nr,nc
    num+=1

for i in tmp:
  print(*i)

