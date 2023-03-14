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
    def isEmpty(self):
        return len(self) == 0
        
    
    # Returns the number of items in the queue.
    def __len__( self ):
        return self._size
    
    # Return but not remove the first item on the queue.
    def first(self):
        assert not self.isEmpty(),"Queue is empty"
        return self._head._item
    

    # Removes and return the first (head of the linked list) item from the queue
    def dequeue(self):
        assert not self.isEmpty(),"Queue is empty"
        curNode = self._head._item
        self._head = self._head._next
        self._size -= 1
        return curNode


    # add a new item onto the last of the queue (tail of the linked list).
    def enqueue( self, item ):
        newNode = ListNode(item)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1
        return self

    # Traversing a linked list
    def __repr__(self):
        curNode = self._head
        s = "["
        while curNode is not None:
            #print(curNode.item)
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
    
# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes
class Array :
# Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear( None )
    # Returns the size of the array.
    def __len__( self ):
        return self._size
    # Gets the contents of the index element.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]
    # Puts the value in the array element at index position.
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value
    def __add__(self,rhsArray):
        assert self._size == rhsArray._size, "Array can't be added"
        newArray = Array(self._size)
        for i in range(self._size):
            newArray[i] = self[i] + rhsArray[i]
        return newArray
    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value
    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )
    # Returns the string reputation of an object
    def __repr__(self):
        s = '[ '
        for x in self._elements:
            s = s + str(x) + ', '
        s = s[:-2] + ' ]'
        return s    
            

# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0
    def __iter__( self ):
        return self
    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration
            
def radixSort( seq, numDigits ): 
     # Create an array of queues to represent the bins. 
     binArray = Array(10) 
     for k in range( 10 ): 
         binArray[k] = LQueue() 
      # The value of the current column. 
     column = 1 
    # Iterate over the number of digits in the largest value. 
     for digit in range( numDigits ): 
        # Distribute the keys across the 10 bins. 
        for key in seq : 
            digit = (key // column) % 10 
            binArray[digit].enqueue( key ) 
        # Gather the keys from the bins and place them back in intList. 
        i = 0 
        for bin in range(len(binArray)) : 
            while not binArray[bin].isEmpty() : 
                seq[i] = binArray[bin].dequeue() 
                i += 1 
        # Advance to the next column value. 
        column *= 10 
     return seq 
 
import time
import random
import matplotlib.pyplot as plt
import pandas as pd

def average(seq, n):
    for i in range(n):
        seq.append(random.randint(0, n))
    return seq
        
def best(seq, n):
    for i in range(n):
        seq.append(i)
    return seq

def worst(seq, n):
    for i in range(n, 0, -1):
        seq.append(i)
    return seq
        
seq1 = []
seq1 = average(seq1, 100)
seq2 = [] 
seq2 = average(seq2, 500)
seq3 = []
seq3 = average(seq3, 1000)
seq4 = [] 
seq4 = average(seq4, 5000)
seq5 = []
seq5 = average(seq5, 10000)

seq11 = []
seq11 = best(seq11, 100)
seq22 = [] 
seq22 = best(seq22, 500)
seq33 = []
seq33 = best(seq33, 1000)
seq44 = [] 
seq44 = best(seq44, 5000)
seq55 = []
seq55 = best(seq55, 10000)

seq111 = []
seq111 = worst(seq111, 100)
seq222 = [] 
seq222 = worst(seq222, 500)
seq333 = []
seq333 = worst(seq333, 1000)
seq444 = [] 
seq444 = worst(seq444, 5000)
seq555 = []
seq555 = worst(seq555, 10000)


###average
start = time.time()
radixSort( seq1, 2 )
end = time.time()
elapsed1 = end - start

start = time.time()
radixSort( seq2, 3 )
end = time.time()
elapsed2 = end - start

start = time.time()
radixSort( seq3, 4 )
end = time.time()
elapsed3 = end - start

start = time.time()
radixSort( seq4, 4 )
end = time.time()
elapsed4 = end - start

start = time.time()
radixSort( seq5, 5 )
end = time.time()
elapsed5 = end - start

###best
start = time.time()
radixSort( seq11, 2 )
end = time.time()
elapsed11 = end - start

start = time.time()
radixSort( seq22, 3 )
end = time.time()
elapsed22 = end - start

start = time.time()
radixSort( seq33, 4 )
end = time.time()
elapsed33 = end - start

start = time.time()
radixSort( seq44, 4 )
end = time.time()
elapsed44 = end - start

start = time.time()
radixSort( seq55, 5 )
end = time.time()
elapsed55 = end - start

###worst
start = time.time()
radixSort( seq111, 2 )
end = time.time()
elapsed111 = end - start

start = time.time()
radixSort( seq222, 3 )
end = time.time()
elapsed222 = end - start

start = time.time()
radixSort( seq333, 4 )
end = time.time()
elapsed333 = end - start

start = time.time()
radixSort( seq444, 4 )
end = time.time()
elapsed444 = end - start

start = time.time()
radixSort( seq555, 5 )
end = time.time()
elapsed555 = end - start




df = pd.DataFrame({
        'n': [100, 500, 1000, 5000, 10000],
        'Time(ave)': [elapsed1, elapsed2, elapsed3, elapsed4, elapsed5],
        'Time(best)': [elapsed11, elapsed22, elapsed33, elapsed44, elapsed55],
        'Time(werst)': [elapsed111, elapsed222, elapsed333, elapsed444, elapsed555]
        })
ax = plt.gca()
df.plot(kind='line',x='n',y='Time(ave)',ax=ax)
df.plot(kind='line',x='n',y='Time(best)',color = 'red', ax=ax)
df.plot(kind='line',x='n',y='Time(werst)',color = 'green', ax=ax)
plt.show()