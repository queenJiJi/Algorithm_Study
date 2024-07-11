import sys

time = []
answer = 0
end_time = 0

n = int(sys.stdin.readline())
for _ in range(n):
    start,end = map(int, sys.stdin.readline().split())
    time.append([start,end])
time.sort(key=lambda x: (x[1],x[0])) # 끝나는 시간을 기준으로 정렬

for t in time:
    if t[0]>=end_time: # 시작시간이 끝나는 시간이랑 같거나 크면(이후시간이면)
        answer+=1 # 가능 강의 스케줄이니 정답
        end_time = t[1] # 끝나는 시간 새로 갱신
print(answer)


