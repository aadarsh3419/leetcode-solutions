class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        count = [0]*n
        enum = list(enumerate(nums))
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            i=j=0
            right_smaller = 0
            while i < len(left) and j < len(right):
                if right[j][1] < left[i][1]:
                    right_smaller+=1
                    merged.append(right[j])
                    j+=1
                else: 
                    count[left[i][0]]+=right_smaller
                    merged.append(left[i])
                    i+=1
            while i<len(left):
                count[left[i][0]]+=right_smaller
                merged.append(left[i])
                i+=1
            merged.extend(right[j:])
            return merged
        merge_sort(enum)
        return count
        
        