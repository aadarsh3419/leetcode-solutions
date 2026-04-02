class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:

        
        current_sum = 0
        for i in range(left,right+1):
            current_sum+=self.nums[i]
        
        
        return current_sum
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)