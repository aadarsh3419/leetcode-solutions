class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arry):
            if len(arry)<=1:
                return arry, 0
            mid = len(arry)//2
            left,left_count =  merge_sort(arry[:mid])
            right,right_count =  merge_sort(arry[mid:])
            count = left_count + right_count
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i]> 2*right[j]:
                    j+=1
                count+=j
            i = j =0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] <=  right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged,count
        result = merge_sort(nums)
        return result[1]
