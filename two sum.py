class Solution(object):
   def twoSum(self, nums, target):      
     
       ans = {}
       i = 0
       j = 0
       count = 0
       
       for i in range(len(nums)):
          for j in range(len(nums)):
             if nums[i] + nums[j] == target :
                count=count+1
                ans.update({count : (i, j)})

       if count==0:
           return "none"

       else:
           return ans
print(Solution().twoSum(nums=[10,20,10,40,50,60,70], target=50))
print(Solution().twoSum(nums=[14, 15, 25, 36, 17, 18, 22, 21], target=39))
print(Solution().twoSum(nums=[4, 10, 6, 14, 18, 19, 20], target=20))
