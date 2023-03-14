def BruteForceStringMatch(T, P):
    n = len(T)
    m = len(P)
    for i in range(0,n-m+1):
    # +1 because range(0,1) is 1 , But we want it to include i at 
    # len(Text)-len(Pattern)
        
        j = 0
        while j < m and P[j] == T[i+j]:
            j = j + 1
        if j == m:
            return i
            
    return -1

T = "HelloPython"
P = "n"
print(BruteForceStringMatch(T, P))

