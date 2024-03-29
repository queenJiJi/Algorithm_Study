# 최대공약수 계산(유클리드 호제법)
# 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘: 유클리드 호제법
# 유클리드 호제법:
# 두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지를 R이라 하자
# 이때 A와B의 최대공약수는 B와 R의 최대공약수와 같음
# 유클리드 호제법의 아이디어를 그대로 재귀함수로 작성 가능

# JiJi's Trick - math 라이브러리 활용하면 GCD(최대공약수) 바로 구함
# import math
# a,b=10,15
# math.gcd(a,b) # 5
# math.lcm(a,b) # 최소공배수(LCM)도 가능(3.9ver이상만 가능 )
# lcm = a*b//math.gcd(a,b) # lcm을 gcd를 통해서 구하기도 가능

def gcd(a, b):  # a>b
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
# print(math.gcd(192, 162))
