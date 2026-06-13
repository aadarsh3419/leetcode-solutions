class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count ={0:1}
        counts = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            x = running_sum - k
            if x in count:
                counts+=count.get(x,0)
            count[running_sum] = count.get(running_sum,0)+1
        return counts


        