from collections import deque

def solution(bridge_length, weight, truck_weights):
  bridge = deque([0]*bridge_length) # 다리의 길이만큼 0으로 초기화
  time = 0 # 총 경과시간
  current_weight = 0 # 현재 다리 위 트럭들의 무게 합

  for truck in truck_weights:
    while True:
      time +=1

      current_weight-=bridge.popleft()  # 다리에서 트럭을 한 대 내림

      if current_weight+truck <= weight: # 새로운 트럭을 다리에 올릴 수 있는지 확인
        bridge.append(truck) # 다리에 새로운 트럭 올리기
        current_weight+=truck 
        break
      else: # 올릴 수 없다면 
        bridge.append(0) # 새로운 트럭을 올릴 수 없으면 빈 공간(0)을 추가
  # 마지막 트럭이 다리를 완전히 건너는 시간 추가
  time += bridge_length

  return time

print(solution(2,10,[7,4,5,6]))