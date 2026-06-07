class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dict = {"*":lambda a,b:a*b,
                "-":lambda a,b:a-b,
                "+":lambda a,b:a+b,
                "/":lambda a,b:int(a/b)}
        for i in tokens:
            if i not in dict:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                result = dict[i](b,a)
                stack.append(result)
        return stack[-1]
