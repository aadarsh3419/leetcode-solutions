class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        e = []
        cur_num = 0
        for i in nums:
            cur_num +=i
            e.append(cur_num)
        return e