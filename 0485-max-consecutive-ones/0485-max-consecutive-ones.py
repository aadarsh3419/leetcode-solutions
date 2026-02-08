class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
            else:
                count = 0
            answer = max(answer,count)
        return answer

                
        