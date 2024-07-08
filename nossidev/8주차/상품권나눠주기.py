from collections import Counter
def solution(gift_cards,wants):
    answer= 0
    # counter = {}
    # for g in gift_cards:
    #     if g in counter:
    #         counter[g] +=1
    #     else:
    #         counter[g] = 1
    counter = Counter(gift_cards)
    print(counter)  
    for want in wants:
        if want in counter and counter[want] > 0:
            counter[want]-=1 # 선물을 가져감
        else:
            answer+=1 # 원하는 선물을 갖지 못하는 사람의 수
    return answer


print(solution([4,5,3,2,1],	[2,4,4,5,1]))
print(solution([5,4,5,4,5],	[1,2,3,5,4]))