s = input()

case0, case1 = 0, 0  # case0: 모두 0으로 변환, case1:모두1로 변환

# 첫번째 원소에 대해서 처리
if s[0] == '1':
    case0 += 1
else:
    case1 += 1

for i in range(1, len(s)):  # 두번째 원소부터 모든 원소 확인
    if s[i-1] != s[i]:
        # 다음 수에서 1로 바뀌는 경우
        if s[i] == '1':
            case0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            case1 += 1
print(case0, case1)
print(min(case0, case1))
