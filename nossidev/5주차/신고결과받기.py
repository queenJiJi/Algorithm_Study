import collections

# SOL 1
# def solution(id_list,report,k):
#   # 신고내역을 저장할 딕셔너리
#   reported_by = collections.defaultdict(set)

#  # 신고내역을 처리
#   for reporting in report:
#     reporter, reported = reporting.split()
#     if reported not in reported_by[reported]: # 중복제거
#       reported_by[reported].add(reporter)

    
#   # 메일을 받게 될 사용자들을 저장할 딕셔너리
#   mail_count = collections.defaultdict(int)

#   # k번 이상 신고된 사용자 처리
#   for reporters in reported_by.values():
#     if len(reporters) >= k:
#       for reporter in reporters:
#         mail_count[reporter] += 1    

#   answer = [mail_count[user] for user in id_list]
#   return answer

# SOL 2
def solution(id_list, report, k):
  answer = [0] * len(id_list)
  # report를 해시셋에 추가해서 중복을 제거하고 시작
  report_set = set(report)

  # 각 id 마다 신고당한 횟수를 저장하는 해시테이블을 생성
  report_dic = {x:0 for x in id_list} # 일단 0으초 초기화
  for r in report_set:
    report_dic[r.split()[1]] += 1

  # report 해시셋을 순회하며 신고대상의 신고당한 횟수가 k를 넘어서는 경우를 찾는다.
  for r in report_set:
    if report_dic[r.split()[1]] >= k:
      # 신고자의 메일 받는 횟수를 1 증가시킨다
      answer[id_list.index(r.split()[0])] += 1

  return answer


print(solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],	3))