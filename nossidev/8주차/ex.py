def solution():
    j = set([7.19, 7.26, 7.27, 7.28, 8.11, 8.17, 8.23, 8.24, 8.25])
    b = set([7.19, 7.20, 7.21, 8.2, 8.3, 8.4, 8.9, 8.10,8.11,8.15,8.16, 8.30, 8.31])
    h = set([7.20,7.27,8.24,8.31])
    answer =  sorted(j&b)
    return '가능한 날 없음' if len(answer)==0 else answer

print(solution())