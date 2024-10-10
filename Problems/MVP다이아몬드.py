n = int(input())  # 개월 수
stdmoney = list(map(int, input().split()))  # 등급 기준 금액
rank = input()  # 각 달의 등급 정보

spent = []
spent[0] = 0
for r in rank:
  if r=='B':
    money =  stdmoney[0] -1
    spent.append(money)
  
  if r=='S':
    money = stdmoney[1] - spent[-1] -1
    spent.append(money)
  
  if r=='G':
    money = stdmoney[2] - spent[-1] -1
    spent.append(money)

  if r=='P':
    money = stdmoney[3] - spent[-1] -1
    spent.append(money)

  if r=='D':
    money = stdmoney[3] 
    spent.append(money)

print(sum(spent))