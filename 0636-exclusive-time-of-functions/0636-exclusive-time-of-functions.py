class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0]*n
        stack = []
        prev = 0
        for log in logs:
            a = log.split(":")
            id = int(a[0])
            type = a[1]
            curr = int(a[2])
            if type == "start":
                if stack:
                    result[stack[-1]] +=curr-prev
                stack.append(id)
                prev = curr
            else:
                result[stack[-1]] += curr-prev+1
                stack.pop()
                prev = curr+1
        return result


 