import sys
n = int(sys.stdin.readline())
A,B = [],[]
answer= float('inf')
for _ in range(n):
  A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
  B.append(list(map(int, sys.stdin.readline().split())))

# 회전
def rotate(A):
  tmp = []
  for i in range(1,n+1):
    tmp.append([i for i in range(i)])

  for i in range(n):
    for j in range(i,n):
      tmp[n-i-1][j-i] = A[j][i]
  return tmp

# 대칭 
def de(origin):
  tmp = [x[::-1] for x in origin]
  return tmp

# 현재와 B의 차이를 계산하는 함수
def Count(A,B):
  cnt=0
  for i in range(n):
    for j in range(i,n):
      if A[j][i]!=B[j][i]:
        cnt +=1
  return cnt

# 회전한 삼각형과 B의 차이 구하기
for i in range(3):
  answer = min(answer,Count(A,B))
  A=rotate(A)

# 대칭한 삼각형과 B의 차이 구하기
for i in range(3):
  answer = min(answer,Count(de(A),B))
  A=de(A)
  A=rotate(de(A))

print(answer)
