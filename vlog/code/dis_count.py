def DistributionCountingSort(array):
    n = len(array)
    k = array[0]
    ans = [0] * n
    
    for i in array:
        if k < i:
            k = i

    count = [0] * (k+1)
    
    for j in array:
        count[j] += 1
        
    for l in range(k):
        x = count[l] + count[l+1]
        count[l+1] = x
        
    array.reverse()
    
    for i in array:
        count[i] -= 1
        ans[count[i]] = i
        
    return ans
    
    
data = [12,13,10,15,17,20,10,19,18,13]
print(DistributionCountingSort(data))