class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = {}
        for i in word:
            dic[i] = dic.get(i,0)+1
        freq = sorted(dic.values(),reverse = True)
        a = 0
        for i in range(len(freq)):
            a+= freq[i] * ((i//8)+1)
        return a
