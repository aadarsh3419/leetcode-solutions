class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dicte = {"*":lambda a,b:a*b,
                 "+":lambda a,b:a+b,
                 "-":lambda a,b:a-b,
                 "/":lambda a,b:int(a/b)
        }
        for i in tokens:
            if i in dicte:
                a = stack.pop()
                b = stack.pop()
                result = dicte[i](b,a)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]
