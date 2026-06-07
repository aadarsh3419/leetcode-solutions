class MinStack:

    def __init__(self):
        
        self.minstack = []
        self.min = []
        

    def push(self, value: int) -> None:
        
        self.minstack.append(value)
        if not  self.min:
            self.min.append(value)
        else:
            self.min.append(min(value,self.min[-1]))
            
 
    def pop(self) -> None:
        self.minstack.pop()
        self.min.pop()
            

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()