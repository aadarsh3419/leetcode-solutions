class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping.values():  # opening brackets
                stack.append(char)
            elif char in mapping:  # closing brackets
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # invalid character
        
        return not stack
