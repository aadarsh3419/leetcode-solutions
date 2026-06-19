class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        close = float("inf")
        best = 0
        for i in range(n):
            j = i + 1
            k = n-1
            while j<k:
                current = nums[i] + nums[j] + nums[k]
                diff = abs(current-target)
                if diff < close:
                    close = diff
                    best = current

                if current > target:
                    k-=1
                elif current < target:
                    j+=1
                else:
                    break
                
        return best