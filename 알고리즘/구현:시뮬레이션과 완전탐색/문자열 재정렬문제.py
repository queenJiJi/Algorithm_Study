s = input()
al_arr= []
num=0
for i in s:
  if i.isalpha():
    al_arr.append(i)
  else:
    i=int(i)
    num+=i

al_arr.sort()
print(''.join(al_arr)+str(num))