# 만들 수 있는 그룹수의 최댓값을 구하는 것
 
n= int(input())
a = list(map(int, input().split()))

group = 0 # 그룹 내 멤버수
count = 0 # 총 그룹 수

a.sort()

for i in a:
  group+=1 # 그룹 내 멤버 추가
  if i<=group: 
    count+=1 # 총 그룹 수 증가시키기
    group =0 # 그룹 초기화


print(count)
