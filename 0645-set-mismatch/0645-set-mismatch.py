class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] <0:
                dup = abs(i)
                output.append(dup)
            else:
                nums[idx]*=-1
        for i in range(len(nums)):
            if nums[i]>0:
                miss = i +1
                output.append(miss)
        return output
                

            