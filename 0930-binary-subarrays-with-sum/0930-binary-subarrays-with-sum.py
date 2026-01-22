class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = {0:1}
        answer = 0
        for j in nums:
            prefix_sum += j
            
            if prefix_sum - goal in count:
                answer += count[prefix_sum - goal]
                
            count[prefix_sum] = count.get(prefix_sum,0)+1
        return answer