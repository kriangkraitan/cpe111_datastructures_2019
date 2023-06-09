# Implementation of the Stack ADT using a Python list.
class Stack :
    # สร้าง stack
    def __init__( self ):
        self._theItems = list()

    # Returns True if the stack is empty or False otherwise.
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the stack.
    def __len__ ( self ):
        return len( self._theItems )
    # Returns the top item on the stack without removing it.
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    def push( self, item ):
        self._theItems.append(item)
        
    # Display items in the stack
    def __repr__(self):
        s = ""
        for item in reversed(self._theItems):
            s = s + "| "+str(item)+" \t|" + "\n"
        s = s+"---------"
        return s
