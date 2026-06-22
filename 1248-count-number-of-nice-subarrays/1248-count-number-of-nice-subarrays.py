class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
        ans = 0
        for num in nums:
            if num %2 !=0:
                prefix+=1
            else:
                0
            print(prefix)
            if prefix - k in count:
                ans+=count[prefix-k]
                print(ans)
            count[prefix] = count.get(prefix,0)+1
        print(count)
        return ans
            