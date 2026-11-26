class Solution:
    def canAliceWin(self, n: int) -> bool:
        a = 10
        alice_turn = True
        while n >= a:
           n-=a
           a-=1
           alice_turn = not alice_turn
        return not alice_turn


        
            
        
            