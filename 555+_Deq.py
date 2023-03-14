class Deque:
    def __init__(self):
        self._dequeList = list()
    
    def AddFirst(self, item):
        self._dequeList.insert(0, item)
        
    def AddRear(self, item):
        self._dequeList.append(item)
        
    def DeleteFirst(self):
        assert not self.isEmpty(), "The deque is empty."
        return self._dequeList.pop(0)
    
    def DeleteRear(self):
        assert not self.isEmpty(), "The deque is empty."
        return self._dequeList.pop()
    
    def First(self):
        assert not self.isEmpty(), "The deque is empty."
        return self._dequeList[0]
        
    def Rear(self):
        assert not self.isEmpty(), "The deque is empty."
        return self._dequeList[-1]
    
    def isEmpty(self):
        return len(self._dequeList) == 0
    
    def length(self):
        return len(self._dequeList)
    
    def __repr__(self):
        s = "<--"
        s=s.join([str(x) for x in self._dequeList])
        return s
        