
start = input()
count = 0  # 경우의 수
# commands = [
#     ['r', 'r', 'u'], ['r', 'r', 'd'], ['l', 'l', 'u'], ['l', 'l', 'd'],
#     ['u', 'u', 'l'], ['u', 'u', 'r'], ['d', 'd', 'l'], ['d', 'd', 'r']]
r, c = int(start[1]), ord(start[0])-ord('a')+1,  # 시작점
# for i in range(8):
#     for j in commands[i]:
#         if j == 'r':
#             c = c + 1
#         if j == 'l':
#             c = c - 1
#         if j == 'u':
#             r = r - 1
#         if j == 'd':
#             r = r + 1

#     if r > 0 and c > 0 and r < 9 and c < 9:
#         count += 1
#     r, c = int(start[1]), ord(start[0])-ord('a')+1
# print(count)

# 개선
commands = [(1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)]
for i in commands:
    nr, nc = r+i[0], c+i[1]
    if nr > 0 and nc > 0 and nr < 9 and nc < 9:
        count += 1
print(count)
