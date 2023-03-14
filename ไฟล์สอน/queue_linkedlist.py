# Implements the Queue ADT using a singly linked list.

# Defines a private storage class for creating list nodes.
class ListNode( object ):
    def __init__( self, item ) :
        self._item = item
        self._next = None

class LQueue :
    # Constructs an empty queue.
    def __init__( self ):
        self._head = None
        self._tail = None
        self._size = 0

    # Return True if the queue is empty or False otherwise.
    def __len__(self):
        return self._size

    # Return True if the Deque is empty or False otherwise
    def isEmpty(self):
        return self._size == 0

    # Return but not remove the first item on the queue.
    def first(self):
        assert not self.isEmpty(),"Queue is empty"
        return self._head._next

    # Removes and return the first (head of the linked list) item from the queue
    def dequeue(self):
        assert not self.isEmpty(),"Queue is empty"
        # Enter Code here
        # ....   
        pass

    # add a new item onto the last of the queue (tail of the linked list).
    def enqueue( self, item ):
        # Enter Code here
        # ....
        pass

    def __repr__(self):
        curNode = self._header
        s = "["
        while curNode is not None:
            s = s + str(curNode._item)+ " "
            curNode = curNode._next
        s = s[:-1] + "]"
        return s
    
    def __str__(self):
        curNode = self._head
        s = "["
        while curNode is not None:
            #print(curNode.item)
            s = s + str(curNode._item)+ " "
            curNode = curNode._next
        s = s[:-1] + "]"
        return s
        
    # Determines if an item is contained in the queue.
    def isContain( self, target ):
        curNode = self._head
        while curNode is not None and curNode._item != target :
            curNode = curNode._next
        return curNode is not None

        
# Code start here
A = LQueue()
A.enqueue(4)
A.enqueue(19)
A.enqueue(23)
A.enqueue(74)
A.enqueue(12)
