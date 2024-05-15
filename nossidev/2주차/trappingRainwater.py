def solution(height):
  result = 0
  l,r = 0, len(height)-1
  leftmax,rightmax = height[l], height[r]

  while l<r:
    if leftmax < rightmax:
      l +=1
      # if leftmax- height[l] <0: # 현재값에서 max값 뺏을때 음수인거면 물을 못모았다는거니까 0을 더해줌 
      #   result +=0
      # else:
      leftmax = max(leftmax, height[l])
      result += (leftmax-height[l])
      

    else: # leftmax>rightmax 
      r -=1
      # if rightmax- height[r] <0:
      #   result +=0
      # else:
      rightmax = max(rightmax,height[r])
      result += (rightmax-height[r])
  return result

print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution([4,2,0,3,2,5]))