# 설명
  # 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제로
  # 이런 유형을 '완전 탐색' 문제 유형이라고 함
  # 가능한 경우의 수를 모두 검사해보는 탐색 방법을 말함
# 아이디어
  # 하루는 86400초 이므로 ,00시 00분 00초 부터 23시 59분 59초까지의 모든 경우의 수는
    # 24*60*60=86400
  # 따라서 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인

n = int(input()) # 0<=n<=23
count =0

for i in range(n+1): # 시
  for m in range(60): # 분
    for s in range(60): # 초
      if '3' in str(i)+str(m)+str(s):
        count+=1
print(count)


