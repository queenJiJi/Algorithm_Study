## Num까지의 소수 구하기

# 1. 단순 반복문
def simple(n):
  result = []
  for i in range(2,n+1):
    is_prime = True
    for j in range(2,i):
      if i%j == 0:
        is_prime = False
        break
    if is_prime:
      result.append(i)
  return result


# 2. loop 도는 횟수 줄이기 - 약수의 갯수가 대칭인 것을 감안하면 제곱근까지만 순회해도 소수인지 아닌지 판별가능
def better(n):
  result = []
  for i in range(2, n+1):
    is_prime= True
    for j in range(2,int(i**(1/2))+1):
      if i%j==0:
        is_prime = False
    if is_prime:
      result.append(i)
  return result

# 3. 에스토스테네스의 체 - 2보다도 더 최적화 된 방법
def best(n):
  primes= set(range(2,n+1)) 

  for num in range(2,int(n**1/2)+1):
    if num in primes:
      primes -= set(range(num**2, n+1, num)) # 전체 prime집합에서 2의배수인 집합들, 3의 배수인 집합들 ,,, 등등 모두 제거 (= 체에 걸러주기) 
  return list(primes)

print(simple(10))
print(better(10))
print(best(10))