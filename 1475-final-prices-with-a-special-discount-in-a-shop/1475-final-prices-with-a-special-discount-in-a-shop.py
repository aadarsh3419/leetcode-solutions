class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        answer = prices.copy()
        for i in range(n):
            while stack and prices[i]<=prices[stack[-1]]:
                index = stack.pop()
                answer[index] = prices[index] - prices[i]
            stack.append(i)
        return answer
        
