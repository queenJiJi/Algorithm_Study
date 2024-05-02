'''
7:00 ~ 19:00 - 1분에 10원
19:00 ~ 7:00 - 1분에 5원
'''
charge=0
for _ in range(int(input())):
  s = input()
  s = s.replace(':',' ')
  h,m,duration = map(int, s.split()) # 전화 시작시간
  end_h, end_m = h,0 # 전화 종료 시간

  if duration+m >= 60: # 시간, 분이 단위를 넘길 시
    end_h = h+1
    end_m = duration + m -60
    if end_h>23:
      end_h = 0
  else:    
    end_h = h
    end_m = m+duration
 
  if (end_h==7 or end_h==19) and m>=end_m and end_m!=0:  # 요금 변환 시간에 통화중일 시
    if end_h == 7: # 7시를 넘길 경우
      charge += (duration-end_m)*5 + end_m*10
    elif end_h == 19 : # 19시를 넘길 경우
      charge += (duration-end_m)*10 + end_m*5
  else: 
    if 7<= h <= 18:
      charge+=duration*10
    else:
      charge+=duration*5

print(charge)


# n = int(input())
# arr =[]
# for _ in range(n):
#   arr.append(input())
# m= len(arr)
# answer =0
# for i in range(m):
#   h = arr[i][0]+arr[i][1]
#   m = arr[i][3]+arr[i][4]
#   d = arr[i][6]+arr[i][7]
#   print(h,m,d)

#   if 7<int(h)<19:
#     if int(h) == 18 and int(m)>30 and int(d) > 30:
#       answer += ((int(d)-30) * 10 + 150)
#     else:
#       answer += int(d)*10
#   else:
#     if int(h) == 6 and int(m)>30 and int(d) >= 30:
#       answer += ((int(d)-30) * 5 + 300)
#     else:
#       answer += int(d) * 5
# print(answer)