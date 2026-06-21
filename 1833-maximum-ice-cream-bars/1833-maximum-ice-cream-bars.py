class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        
        a = 0
        count = 0
        
        for i in range(n):
            print(a)
            if a + costs[i] <= coins:
                a += costs[i]
                
                count +=1 
            else:
                break
        
        return count            
