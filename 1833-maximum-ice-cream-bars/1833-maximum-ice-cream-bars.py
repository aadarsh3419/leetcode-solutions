class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)
        if sum(costs) <= coins:
            return n
        a = 0
        count = 0
        for i in range(n):
            
            if a <= coins:
                a += costs[i]
                
                count +=1 
            else:
                break
        return count - 1           
