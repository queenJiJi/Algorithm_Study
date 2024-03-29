n=int(input())
arr = [500,100,50,10]
count = 0


for coin in arr:
  count+=n//coin
  n%=coin

print(count)