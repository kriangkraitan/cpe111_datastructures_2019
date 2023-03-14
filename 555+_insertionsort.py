import time
import random
import matplotlib.pyplot as plt
import pandas as pd
start = time.time()
theSeq = []
for i in range(0,100):
    theSeq.append(random.randint(0, 100))
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed1 = end - start
print(elapsed1)

start = time.time()
theSeq = []
for i in range(0,500):
    theSeq.append(random.randint(0, 500))
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed2 = end - start
print(elapsed2)

start = time.time()
theSeq = []
for i in range(0,1000):
    theSeq.append(random.randint(0, 1000))
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed3 = end - start
print(elapsed3)

start = time.time()
theSeq = []
for i in range(0,5000):
    theSeq.append(random.randint(0, 5000))
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed4 = end - start
print(elapsed4)

start = time.time()
theSeq = []
for i in range(0,10000):
    theSeq.append(random.randint(0, 10000))
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed5 = end - start
print(elapsed5)

##best
start = time.time()
theSeq = []
for i in range(0,100):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed11 = end - start


start = time.time()
theSeq = []
for i in range(0,500):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed22 = end - start

start = time.time()
theSeq = []
for i in range(0,1000):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed33 = end - start

start = time.time()
theSeq = []
for i in range(0,5000):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed44 = end - start

start = time.time()
theSeq = []
for i in range(0,10000):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed55 = end - start

##worst
start = time.time()
theSeq = []
for i in range(100,0, -1):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed111 = end - start


start = time.time()
theSeq = []
for i in range(500,0, -1):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed222 = end - start

start = time.time()
theSeq = []
for i in range(1000,0, -1):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed333 = end - start

start = time.time()
theSeq = []
for i in range(5000,0, -1):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed444 = end - start

start = time.time()
theSeq = []
for i in range(10000,0, -1):
    theSeq.append(i)
def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
    return theSeq

insertionSort(theSeq)
end = time.time()
elapsed555 = end - start

df = pd.DataFrame({
        'n': [100, 500, 1000, 5000, 10000],
        'Time(ave)': [elapsed1, elapsed2, elapsed3, elapsed4, elapsed5],
        'Time(best)': [elapsed11, elapsed22, elapsed33, elapsed44, elapsed55],
        'Time(werst)': [elapsed111, elapsed222, elapsed333, elapsed444, elapsed555]})
    
  
ax = plt.gca()
df.plot(kind='line',x='n',y='Time(ave)',ax=ax)
df.plot(kind='line',x='n',y='Time(best)',color = 'red', ax=ax)
df.plot(kind='line',x='n',y='Time(werst)',color = 'black', ax=ax)
plt.show()
