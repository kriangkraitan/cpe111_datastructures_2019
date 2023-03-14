import time
import random
import matplotlib.pyplot as plt
import pandas as pd
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

    
        
     
        
###average
start = time.time()
seq = []
for i in range(100):
    seq.append(random.randint(0, 100))
merge_sort(seq)
end = time.time()
elapsed1 = end - start


start = time.time()
seq = []
for i in range(0,500):
    seq.append(random.randint(0, 500))
merge_sort(seq)
end = time.time()
elapsed2 = end - start


start = time.time()
seq = []
for i in range(0,1000):
    seq.append(random.randint(0, 1000))
merge_sort(seq)
end = time.time()
elapsed3 = end - start


start = time.time()
seq = []
for i in range(0,5000):
    seq.append(random.randint(0, 5000))
merge_sort(seq)
end = time.time()
elapsed4 = end - start


start = time.time()
seq = []
for i in range(0,10000):
    seq.append(random.randint(0, 10000))
merge_sort(seq)
end = time.time()
elapsed5 = end - start



###best

start = time.time()
seq = []
for i in range(0,100):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed11 = end - start

start = time.time()
seq = []
for i in range(0,500):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed22 = end - start


start = time.time()
seq = []
for i in range(0,1000):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed33 = end - start

start = time.time()
seq = []
for i in range(0,5000):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed44 = end - start


start = time.time()
seq = []
for i in range(0,10000):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed55 = end - start


###werst

start = time.time()
seq = []
for i in range(100,0, -1):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed111 = end - start


start = time.time()
seq = []
for i in range(500,0, -1):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed222 = end - start



start = time.time()
seq = []
for i in range(1000,0, -1):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed333 = end - start


start = time.time()
seq = []
for i in range(5000,0, -1):
    seq.append(i)
merge_sort(seq)
end = time.time()
elapsed444 = end - start


start = time.time()
seq = []
for i in range(10000,0, -1):
    seq.append(i)
merge_sort(seq)
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
df.plot(kind='line',x='n',y='Time(werst)',color = 'pink', ax=ax)
plt.show()







