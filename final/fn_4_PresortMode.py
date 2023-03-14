def merge(left, right, seq):
    i = j =0
    while i + j < len(seq): 
        if j == len(right) or (i < len(left) and left[i] < right[j]): 
            seq[i+j] = left[i] # copy ith element of left as next item of seq
            i+=1
        else:            
            seq[i+j] = right[j] # copy jth element of right as next item of seq 9            
            j += 1 
def merge_sort(seq): 
    n = len(seq) 
    if n < 2: 
          return "list is already sorted"
    # divide 
    mid = n // 2 
    left = seq[0:mid] # copy of first half 
    right = seq[mid:n] # copy of second half 
    # conquer (with recursion) 
    merge_sort(left) # sort copy of first half 
    merge_sort(right) # sort copy of second half 22    # merge results 
    seq = merge(left, right, seq) 
    return seq 

def PresortMode(A):
    n = len(A)
    merge_sort(A)
    i = 0
    modefrequency = 0
    while i <= (n-1):
        runlength = 1
        runvalue = A[i]
        while i + runlength <= (n-1) and A[i + runlength ] == runvalue:
            runlength = runlength + 1
        if runlength > modefrequency:
            modefrequency = runlength
            modevalue = runvalue
        i = i + runlength
    return modevalue

A = [2,3,4,4,5,3,2,6,16,5,6,7,10,12,12,6,6,2,3,4]
print(PresortMode(A))