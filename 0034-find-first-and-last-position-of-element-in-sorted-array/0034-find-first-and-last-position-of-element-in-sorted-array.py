class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        
        a = -1
        
        while left <= right:
            
            mid = (left + right) // 2
            if nums[mid] == target:
                a = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        l = 0
        r = len(nums) - 1
        b = -1
        while l <= r:
            mid =(l+r)//2
            if nums[mid] == target:
                b = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
            
            
        return [a,b]
            