n = input()
left_sum, right_sum = 0, 0

for i in range(0, len(n)//2):
    left_sum += int(n[i])

for i in range(len(n)//2, len(n)):
    right_sum += int(n[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')

# sol2  -- 슬라이싱 풀이
# n = list(map(int, input()))
# left_sum = sum(n[:len(n)//2])
# right_sum = sum(n[len(n)//2:])
# if left_sum == right_sum:
#     print('LUCKY')
# else:
#     print('READY')
