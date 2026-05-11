class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = []

        for i in nums:
            n.extend([int(i) for i in str(i)])
        return n