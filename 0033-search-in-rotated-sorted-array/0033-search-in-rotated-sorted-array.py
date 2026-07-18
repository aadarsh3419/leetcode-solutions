class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left<right:
            mid = (left+right+1)//2
            if nums[mid] >=nums[0]:
                left = mid
            else:
                right  = mid - 1
        m = left
        left = 0
        right = m
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        l = m + 1
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:  
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
