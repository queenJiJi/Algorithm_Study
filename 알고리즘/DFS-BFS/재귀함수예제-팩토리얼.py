# 팩토리얼 구현 예제
# 0!,1! = 1 임

# 반복문으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result


# 재귀함수로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1이하인 경우 1을 반환
        return 1
    # n!=n*(n-1)!를 그대로 코드로 작성하기
    return n*factorial_recursive(n-1)


# 반복문과 재귀함수로 구현한 n! 출력(n=5)
print('반복', factorial_iterative(5))
print('재귀', factorial_recursive(5))
