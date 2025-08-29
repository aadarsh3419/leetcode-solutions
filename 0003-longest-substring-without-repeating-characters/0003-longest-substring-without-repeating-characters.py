class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()      # to store unique chars in current window
        left = 0          # left pointer of the window
        max_len = 0

        for right in range(len(s)):
            # if char is repeated, move left until it's unique
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
