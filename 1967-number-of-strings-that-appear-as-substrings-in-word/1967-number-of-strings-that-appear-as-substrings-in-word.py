class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for patt in patterns:
            if patt in word:
                count+=1
        return count