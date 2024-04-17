s = input()

sum = 0
line = ''
for i in s:
    if i.isdigit():
        sum += int(i)
    else:
        line += i
print(''.join(sorted(line))+str(sum))
