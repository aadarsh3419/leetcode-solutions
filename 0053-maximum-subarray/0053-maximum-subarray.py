class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
           current_sum = arr[0]
           max_sum = arr[0]
           for i in range(1,len(arr)):
             current_sum = max(arr[i],current_sum + arr[i])
             max_sum = max(max_sum,current_sum)
           return max_sum
        