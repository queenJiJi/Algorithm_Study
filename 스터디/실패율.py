def solution(N,stages):
    all_user = len(stages)
    count =[0] * (N+2)
    for i in stages:
        count[i]+=1
    fail = []
    for step in range(1,N+1):
        # cnt = stages.count(step)
        if all_user == 0:
            fail.append((step,0))
        else:
            fail.append((step, (count[step] /all_user)))
            all_user -= count[step]

    fail.sort(key=lambda x : (-x[1],x[0])) # 두번째 요소를 기준으로 내림차순 정렬 후, 동일한 경우 첫번째 요소를 오름차순 정렬

    return [x[0] for x in fail]

print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))