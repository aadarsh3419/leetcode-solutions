class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        a = arr.index(max(arr))
        if a == 0 or a == n-1:
            return False
        for i in range(a):
            if arr[i] >= arr[i+1]:
                return False

        for i in range(a,n-1):
            if arr[i] <= arr[i+1]:
                return False

        return True