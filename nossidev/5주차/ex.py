def solution(id_list, report, k):
    # ✅ report를 해시셋에 추가해 중복을 제거한다.
    report_set = set(report)
    answer = [0] * len(id_list)

    # ✅ 각 id마다 신고당한 횟수를 저장하는 해시테이블을 생성한다.
    reports = {x: 0 for x in id_list}
    for r in report_set:
        reports[r.split()[1]] += 1
    print(reports)

    for r in report_set:
        # ✅ report 해시셋을 순회하며 신고대상의 신고당한 횟수가 k를 넘어서는 경우를 찾는다.
        if reports[r.split()[1]] >= k:
            # ✅ 신고자의 메일 받는 횟수를 1 증가시킨다.
            print(r.split()[0])
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],	3))