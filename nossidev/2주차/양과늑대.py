def solution(info, edges):
  
  visited = [0] * len(info) # 노드들 방문 체크하는 배열 선언
  answer = [] # 양의 수를 노드 돌때마다 업데이트 

  def backtrack(sheep_num, wolf_num):
    # base case
    if wolf_num < sheep_num: # 양의 수가 늑대수보다 적다면 계속 전진-> 양의 수 업데이트
      answer.append(sheep_num)
    else:# 만약 늑대가 양보다 크거나 같으면 빠져나오기
      return
    
    for parent,child in edges: #[부모노드, 자식 노드]
      if visited[parent] and not visited[child]:# 부모노드는 방문했는데 자식노드는 방문하지 않은 상태라면 방문시작
        visited[child] = True # 다음 노드를 방문 표시 
        if info[child] == 0: # 다음 노드가 양이라면 sheep의 갯수 +1
          backtrack(sheep_num+1, wolf_num)
        else: # 다음 노드가 늑대라면 
          backtrack(sheep_num,wolf_num+1)
        visited[child] = False # 다음 노드 방문 표시 해제
  visited[0] = True # 루트노드는 항상 양이므로 0번 노드는 방문한 상태로 시작
  backtrack(1,0) #루트노드는 항상 양이므로 1마리 먼저 시작하는 것으로 설정   

  return max(answer) # 양의 수 업데이트 한것 들 중 가장 양의 수가 큰 것 return




print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))



