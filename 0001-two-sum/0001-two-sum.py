class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        mp = {}
        
        for i in range(n):
            x=0
            x =  target -nums[i]
            if x in mp:
                return [mp[x],i]
            mp[nums[i]] = i