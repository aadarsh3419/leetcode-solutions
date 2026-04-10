class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt = {}
        for num in nums:
            dictt[num] = dictt.get(num,0)+1
        return max(dictt,key =dictt.get)
