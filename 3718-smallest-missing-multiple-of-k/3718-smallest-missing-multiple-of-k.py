class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        dic = {}
        for i in nums:
            if i%k == 0:
                dic[i] = dic.get(0,i)+1
        
        print(dic)
        i = 1
        while True:
            a = k*i
            print(a)
            print(a)
            if a not in dic:
                return a 
            i+=1
            
