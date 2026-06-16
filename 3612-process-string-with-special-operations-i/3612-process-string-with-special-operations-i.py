class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)
        result = ""
        graph = dict(zip(map(chr,range(95,123)),map(chr,range(95,123))))
        for i in range(n):
            if s[i] in graph:
                result += s[i]
            if s[i] == "*":
                if result:
                    result = result[:-1]
            if s[i] == "#":
                if result:
                    result += result
            if s[i] =="%":
                result = result[::-1]
        return result