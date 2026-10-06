class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        visit = {}
        def dp(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in visit:
                return visit[target]
            result = 0
            for i in nums:
                ds = dp(target-i)
                result+=ds
            visit[target] = result
            return visit[target]
        return dp(target)
            