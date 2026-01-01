class Solution:
    def shuffle(self, nums: List[int], n: int):
        new_nums = []
        for i in range(n):
            if nums == 0:
                return "empty"
            new_nums.append(nums[i])
            new_nums.append(nums[i+n])
        return new_nums
            
        