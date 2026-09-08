class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        while left < right:
            a = numbers[left] + numbers[right]
            if a == target:
                return (left+1,right+1)
            elif a > target:
                right-=1
            elif a < target:
                left+=1
        return 0


                 