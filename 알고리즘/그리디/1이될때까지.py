a,b=map(int, input().split())
count = 0

# while a>0:
#   if a%b==0:
#     count+=1
#     a//=b
#   else:
#     a-=1
#     count+=1
# print(count-1)



# 정답 --> 시간복잡도가 log(n)으로 굉장히 빠른 편
# a가 굉장히 큰 수일때는 위에 내가 짠대로 하면 시간복잡도가 너무 높으니 아래처럼
# 일단 a를 최대한 나눠서 a를 작은 수로 만든 다음 진행해야함
while True:
  # a가 b로 나누어 떨어지는 수가 될 때까지 빼기
  target = (a//b)*b
  print(target)
  count+=(a-target)

  # a가 b보다 작을 때(더이상 나눌수없을때) 반복문 탈출
  if a<b:
    break
  #b로 나누기
  count+=1
  a//=b

# 마지막으로 남은 수에 대하여 1씩빼기
  count+=(a-1)
  print(count)