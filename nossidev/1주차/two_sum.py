class Solution:
    def twoSum():
        target = 13
        nums =[4,9,7,5,1]
        # SOL1 - Brute Force
        # n = len(nums)
        # for i in range(n-1): 
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        # return []

        # SOL2 - Hashmap
        hashmap= {}
        n= len(nums)
        for i in range(n):
            hashmap[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in hashmap and i!=hashmap[complement]:
                return [i, hashmap[complement]]
        return []
        
        
        # SOL3 - Backtracking
        # def backtracking(start):
				#   if len(ans) == 2: # 재귀 2번도니까 
				#     if nums[ans[0]]+nums[ans[1]] == target:
				#       # print(nums[ans[0]],nums[ans[1]])
				#       return ans
				#     return False
				  
				#   for i in range(start,n):
				#     ans.append(i)
				  
				#     if backtracking(i+1):
				#       return ans
				    
				#     ans.pop()
				
				# print(backtracking(0))
        
        
		