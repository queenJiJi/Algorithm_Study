from itertools import combinations
def solution(needs,r):
    answer = 0
    case = len(needs[0])
    case_col = list(combinations(range(0,case), r))

    for c in case_col:
        c=set(c)
        count = 0
        for need in needs:
            for i,val in enumerate(need):
                if i not in c and val==1: # val이 1인데 그 val의 인덱스값이 c에 포함되지 않았다면 break
                    break
            else:  #만약 가장 안쪽 루프가 break에 도달하지 않으면 
                # (즉, 모든 1이 열 조합: [1,0,0],[1,1,0],... c에 포함된 경우), count를 1 증가시킴
                count+=1
        answer = max(answer,count)
    return answer


print(solution([[1,0,0],[1,1,0],[1,1,0],[1,0,1],[1,1,0],[0,1,1]],2))