s=input()

result = 1
for i in range(len(s)):
  a=int(s[i])
  if a==0 or a==1:
    result += a
    i+=1
  else:
    result *= a
print(result)
