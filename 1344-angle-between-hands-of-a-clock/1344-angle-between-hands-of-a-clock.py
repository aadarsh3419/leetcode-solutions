class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = 30
        b = 5.5
        ans = abs((a*hour) - (b*minutes))
        if ans > 180:
            ans = abs(ans -360)
        return ans