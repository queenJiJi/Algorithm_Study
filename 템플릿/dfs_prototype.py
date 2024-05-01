# dfs 구현법은 : *1. recursion  or 2. stack

graph = {
  'A':['B','D','E'],
  'B':['A','C','D'],
  'C':['B'],
  'D':['A','B'],
  'E':['A']
}

visited=[]

def dfs(start_v):
  visited.append(start_v)
  for i in graph[start_v]:
    if i not in visited:
      dfs(i)
  return visited

print(dfs('A'))
  
