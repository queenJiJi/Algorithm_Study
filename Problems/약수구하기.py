### 1부터 number까지 약수의 갯수를 return하라 
# 기본 방법 
def solution(number):
  result = []
  for i in range(1,number+1):
    cnt = 0
    for j in range(1,i+1):
      if i%j==0:
        cnt+=1
    result.append(cnt)
  return result


# 최적화 - 약수의 갯수의 대칭성을 고려 -> 루프가 갯수의 반만큼만 도니까 훨씬 시간복잡도가 줄어듬
def better_sol(number):
  result = []

  for num in range(1,number+1):
    cnt = 0
    for i in range(1, int(num**(1/2))+1): # 제곱근까지만 
      if num%i==0:
        cnt+=1
        if i**2 != num: # 25의 약수는 5,5인데 5가 두번 들어가면 안되니까 그런경우가 아니라면 약수가 2개씩 짝일테니 한번더 더해주기
          cnt+=1
    result.append(cnt)
  return result


print(solution(10))
print(better_sol(10))