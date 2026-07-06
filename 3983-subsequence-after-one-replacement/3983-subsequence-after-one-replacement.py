class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        j = 0
        for ch in t:
            # is line mai ham j ko update karengai aagar vo value hamai mil gayi t mai to 
            if j<n and s[j] == ch:
                j+=1
            # is line mai ham check karengai kii ham replace kar saktai hai ya nhi aagar ham kar saktai hai to kar dengai ismai ham i kii state badal rha hai normali aagar chalegai to mostly j same rhaga but difference tab ayga jab koi character match nhi hoga or fir ham j ko artificaliy move kar dengai
            j = max(j,i+1)
            # ismai bhi ham yahi check kar rha hai kii character match hua ya nhi 
            if i<n and s[i] == ch:
                i+=1
        return j >= n