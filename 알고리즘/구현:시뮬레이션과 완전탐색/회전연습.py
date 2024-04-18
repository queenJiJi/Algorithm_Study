A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def decalco(arr):  # 배열 좌우 반전
    new = [arr[i][::-1] for i in range(3)]
    return new


def upside_down(arr):  # 배열 상하 반전
    # new = [i for i in arr[::-1]]
    arr.reverse()
    return arr


def rotate90(arr):  # 배열 90도 회전
    new = [i[::-1] for i in list(zip(*arr))]
    return new


def rotate180(arr):  # 배열 180도 회전 = 상하반전 + 좌우 반전
    new = [i for i in arr[::-1]]
    new = [i[::-1] for i in new]
    return new


def rotate270(arr):  # 배열 270도 회전 = 왼쪽 90도 회전
    new = [i for i in list(zip(*arr))[::-1]]
    return new


def rotate360(arr):  # 배열 360도 회전
    new = [i for i in arr]
    return new


def rotate_n_deg(n, arr):  # 오른쪽 90도를 n번 반복 -> 1번: 90도, 2번: 180도, 3번: 270도, 4번: 360도
    new_A = arr
    for _ in range(n):
        new_A = [i[::-1] for i in list(zip(*new_A))]
    return new_A


print('좌우반전: ', decalco(A))
print('상하반전: ', upside_down(A))
print('오른쪽90: ', rotate90(A))
print('오른쪽180: ', rotate180(A))
print('오른쪽270: ', rotate270(A))
print('360회전: ', rotate360(A))
print()
print(rotate_n_deg(4, A))
