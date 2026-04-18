class Solution:
    def jump(self, nums: List[int]) -> int:
      n = len(nums)
      current_end = 0
      fur = 0
      jump = 0
      for i in range(n-1):
        fur = max(fur,i+nums[i])
        if current_end == i:
            jump+=1
            current_end = fur
      return jump