class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ops = []
        idx = 0
        for i in range(1,n+1):
            stack.append(i)
            if idx == len(target):
                break
            ops.append("Push")
            if idx < len(target) and i == target[idx]:
                idx +=1
            else:
                stack.pop()
                ops.append("Pop")
        return ops