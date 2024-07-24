coin = [500,100,50,10]
money = 1260
count = 0
for c in coin:
  count+= money//c
  print('count',count)
  money%=c
print(count)