class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        array = []
        
        for i in range(n-k+1):
            diff = nums[i+k-1] - nums[i]
            array.append(diff)
                
        return min(array)