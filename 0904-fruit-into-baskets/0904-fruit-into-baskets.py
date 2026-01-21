class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        answer = 0
        i = 0
        f = len(fruits)

        for j in range(f):
            count[fruits[j]] = count.get(fruits[j],0)+1
            
            while len(count)>2:

                count[fruits[i]]-=1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i+=1
            answer = max(answer,j-i+1)
        return answer