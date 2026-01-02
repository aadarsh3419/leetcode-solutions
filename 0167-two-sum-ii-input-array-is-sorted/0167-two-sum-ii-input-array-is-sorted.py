class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        e = []
        while i<j:
            s = numbers[i]+numbers[j]
            if target == s:
                e = i+1,j+1
                return e
            elif  s>target:
                j-=1
            elif  s<target:
                i+=1
            
        

                 