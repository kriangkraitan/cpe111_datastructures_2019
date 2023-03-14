# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes
class Array :
    # สร้าง array โดยมี element เป็นขนาดของ array
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
    # แสดงค่าของ array ในตำแหน่งนั้นๆ (element คือ ตำแหน่ง หรือ index)
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]
    # แทนที่ค่าของตำแหน่งนั้นๆ element คือ index และ value ที่ต้องการเอาไปแทนที่
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value
    # บวก array
    def __add__(self,rhsArray):
        assert self._size == rhsArray._size, "Array can't be added"
        newArray = Array(self._size)
        for i in range(self._size):
            newArray[i] = self[i] + rhsArray[i]
        return newArray
    # แทนที่ค่าที่ต้องการในทุกตำแหน่ง.
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

# Implementation of the Array2D ADT using an array of arrays.
class Array2D :
    # Creates a 2-D array of size numRows x numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )
        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ) :
            self._theRows[i] = Array( numCols )
    # Returns the number of rows in the 2-D array.
    def numRows( self ):
        return len( self._theRows )
    # Returns the number of columns in the 2-D array.
    def numCols( self ):
        return len( self._theRows[0] )
    # Clears the array by setting every element to the given value.
    def clear( self, value ):
        for row in range( self.numRows() ):
            #row_.clear( value )
            self._theRows[row].clear(value)
    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1] 
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]
    # Sets the contents of the element at position [i,j] to value.
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value
    # Returns the string reputation of an object
    def __repr__(self):
        s = ""
        for r in self._theRows:
            s = s + str(r) + "\n" 
        s = s[:-2] + "]"
                
        return s


class Matrix(Array2D):
    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar):
        for r in range(self.numRows()):
            for c in range( self.numCols()):
                self[ r, c ] *= scalar
        return self[r,c]

    # Creates and returns a new matrix that is the transpose of this matrix.
    def tranpose( self ):
        newMatrix = Matrix(self.numCols(), self.numRows())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c, r] = self[r, c]

        return newMatrix
        # Creates and returns a new matrix that results from matrix addition.    
    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
        rhsMatrix.numCols() == self.numCols(), \
        "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]
        return newMatrix
        
    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__( self, rhsMatrix ):
        assert self.numCols() == rhsMatrix.numRows(), \
               "Matrix size not compatible for the multiple operation"
        newMatrix = Matrix( self.numRows(),rhsMatrix.numCols())
        for r in range(newMatrix.numRows()):
            for c in range(self.numCols()):
                for i in range(self.numCols()):
                    newMatrix[r,c] += self[r,i] * rhsMatrix[i,c]
        return newMatrix
    def det(self):
        if len( self._theRows ) == len( self._theRows[0] ) == 2:
            return self._theRows[0][0]*self._theRows[1][1] - self._theRows[0][1]*self._theRows[1][0]
        elif len( self._theRows ) == len( self._theRows[0] ) == 3:
            u = self._theRows[0][0]*self._theRows[1][1]*self._theRows[2][2] + self._theRows[0][1]*self._theRows[1][2]*self._theRows[2][0] + self._theRows[0][2]*self._theRows[1][0]*self._theRows[2][1]
            l = self._theRows[2][0]*self._theRows[1][1]*self._theRows[0][2] + self._theRows[2][1]*self._theRows[1][2]*self._theRows[0][0] + self._theRows[2][2]*self._theRows[1][0]*self._theRows[0][1]
            return u-l
        else:
            return "Error"
    
    def inverse(self):
        assert len( self._theRows ) == len( self._theRows[0] ) == 2, \
                " For Matrix 2*2 "
        scala = 1 / self.det()
        newMatrix = Matrix(2,2)
        newMatrix._theRows[0][0] = self._theRows[1][1]
        newMatrix._theRows[0][1] = -self._theRows[0][1]
        newMatrix._theRows[1][0] = -self._theRows[1][0]
        newMatrix._theRows[1][1] = self._theRows[0][0]
        for r in range(2):
            for c in range(2):
                newMatrix._theRows[r][c] *= scala 
        return newMatrix
        
#---------------test det ----------------
a = Matrix(2,2)
a.clear(0)
a.clear(1)
a.__setitem__((1,1),2)
print(a,"\n")
#print(a.scaleBy(1))
print(a.det())
print(a.inverse())
b = Matrix(3,3)
b.clear(1)
#print(b.inverse())
##print(b)
##print(b.det())
#c = Matrix(3,2)
#c.clear(1)
##print(c.det())

A = Matrix(2,2)
A[0,0] = 1
A[0,1] = 1
A[1,0] = 1
A[1,1] = 1



B = Matrix(2,2)
B[0,0] = 1
B[0,1] = 1
B[1,0] = 1
B[1,1] = 1




