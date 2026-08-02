class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix = []
        arry = []
        a = 0
        for i in tasks:
            a+=i
            prefix.append(a)
        total = prefix[-1]
        p  = 0
        
        for i in range(len(shifts)):
            if p+shifts[i]>=total:
                arry.append(0)
                p= 0
                
            else:
                p+=shifts[i]
                left = 0
                right = len(tasks) - 1
                pos = len(tasks)
                while left<=right:
                    mid = (left + right)//2
                    if prefix[mid] > p:
                        pos = mid
                        right = mid - 1    
                    else :
                        left = mid + 1
                arry.append(len(tasks)-pos)
        return arry
                 