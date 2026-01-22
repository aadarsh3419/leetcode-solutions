class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix_sum = 0
        answer = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum - k in count:
                answer+= count[prefix_sum - k]
            count[prefix_sum] = count.get(prefix_sum,0)+1
               
        return answer
                