# 여러 대의 서버로 부하를 분산하는 로드밸런서를 만들고자 합니다. 
# 해당 로드밸런서는 기본적으로는 라운드 로빈 방식으로 요청을 서버로 분배합니다. 
# 다만 요청의 sticky 옵션이 `true`인 경우 이전에 분배된 서버로 요청이 분배되어야 합니다. 
# 이러한 동작을 수행하는 함수를 구현해보세요.

# - 라운드 로빈 방식 : 1번 서버부터 시작, 1, 2, ... N, 그리고 다시 1, 2, ... 순서입니다.



def solution(num_servers, sticky, requests):
  servers = [[] for _ in range(num_servers)]

  if not sticky:
    for i, req in enumerate(requests):
      server_idx= i % num_servers
      servers[server_idx].append(req) 
  else:
      cur_server_idx = 0
      server_dic = {}
      for req in requests:
        if req in server_dic:
            server_idx= server_dic[req]
        else:
           server_idx = cur_server_idx % num_servers
           server_dic[req] = server_idx
           cur_server_idx+=1
        servers[server_idx].append(req) 
      
  return servers

print(solution(2,	False,	[1, 2, 3, 4])) #[[1, 3], [2, 4]]
print(solution(2,	True,	[1, 1, 2, 2])) #[[1, 1], [2, 2]]
print(solution(2,	True,	[1, 2, 2, 3, 4, 1])) #[[1, 3, 1], [2, 2, 4]]
