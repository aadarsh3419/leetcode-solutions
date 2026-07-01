class Solution:
    def isPalindrome(self, s: str) -> bool:
       word ="".join(char.lower() for char in s if char.isalnum())
       if word == word[::-1]:
        return True
       else:
        return False