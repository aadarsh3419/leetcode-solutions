class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs((30*hour) - (5.5*minutes))
        if ans > 180:
            ans = abs(ans -360)
        return ans