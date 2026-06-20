class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
     
        ans = 0
        for num in nums:
            prefix+=num
            old = prefix % k
            if old in count:
                ans+=count.get(old,0)
                print(ans)
            count[old] = count.get(old,0)+1
        return ans

 