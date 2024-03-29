from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))

    print('l is:', l)
    print('s is:', s)
    return s.count(target)


print(solution([1, 1, 1, 1, 1],	3))
print(solution([4, 1, 2, 1],	4))
