class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        a = n-k
        b = []
        for i in range(a,n):
            b.append(nums[i])
        for i in range(0,a):
            b.append(nums[i])
        for i in range(n):
            nums[i] = b[i]
        return nums


        
